"""Price an estimate against private studio rates.

Reads rates from the private vault (``$THREEW_VAULT/rates.yaml``, default
``~/3rdwrong-vault/rates.yaml``) or ``--rates PATH`` and an estimate YAML,
then prints price options, margin, effective hourly rate, payment schedule
and a go/no-go to stdout. It never writes files: money stays in the vault.
See business/pricing/rates-and-estimates.md for both formats.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


class PricingError(ValueError):
    pass


def vault_dir() -> Path:
    return Path(os.environ.get("THREEW_VAULT") or Path.home() / "3rdwrong-vault").expanduser()


def load_yaml(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise PricingError(f"file not found: {path}") from None
    except yaml.YAMLError as exc:
        raise PricingError(f"invalid YAML in {path}: {exc}") from None
    if not isinstance(data, dict):
        raise PricingError(f"{path} must contain a YAML mapping")
    return data


def _number(value: object, where: str, *, low: float = 0.0, high: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise PricingError(f"{where} must be a number")
    if value < low or (high is not None and value > high):
        bound = f"between {low} and {high}" if high is not None else f"at least {low}"
        raise PricingError(f"{where} must be {bound}")
    return float(value)


def validate_rates(rates: dict) -> dict:
    roles = rates.get("roles")
    if not isinstance(roles, dict) or not roles:
        raise PricingError("rates: 'roles' must be a non-empty mapping")
    for name, role in roles.items():
        if not isinstance(role, dict):
            raise PricingError(f"rates: role '{name}' must be a mapping")
        _number(role.get("cost_per_hour"), f"rates: roles.{name}.cost_per_hour")
        _number(role.get("rate_per_hour"), f"rates: roles.{name}.rate_per_hour")
    _number(rates.get("overhead_rate", 0), "rates: overhead_rate", high=5)
    target = _number(rates.get("target_margin"), "rates: target_margin", high=0.95)
    floor = _number(rates.get("floor_margin", target), "rates: floor_margin", high=target)
    _number(rates.get("tax_set_aside", 0), "rates: tax_set_aside", high=1)
    _number(rates.get("rounding", 1), "rates: rounding", low=1)
    rates.setdefault("floor_margin", floor)
    validate_schedule(rates.get("payment_schedule"), "rates: payment_schedule")
    return rates


def validate_schedule(schedule: object, where: str) -> list[dict]:
    if not isinstance(schedule, list) or not schedule:
        raise PricingError(f"{where} must be a non-empty list of {{milestone, share}}")
    total = 0.0
    for index, item in enumerate(schedule, start=1):
        if not isinstance(item, dict) or not item.get("milestone"):
            raise PricingError(f"{where} item {index} needs a 'milestone'")
        total += _number(item.get("share"), f"{where} item {index} share", high=1)
    if not math.isclose(total, 1.0, abs_tol=1e-6):
        raise PricingError(f"{where} shares must sum to 1 (got {total:g})")
    return schedule


@dataclass
class Option:
    name: str
    label: str
    stages: list[str]
    hours: float
    labour_cost: float
    overhead: float
    expenses: float
    total_cost: float
    rate_price: float
    floor_price: float
    price: float
    value_priced: bool
    gross_margin: float
    effective_hourly: float
    first_stage_cash: float
    hours_by_role: dict[str, float] = field(default_factory=dict)


def round_up(value: float, step: float) -> float:
    return math.ceil(value / step - 1e-9) * step


def price_estimate(rates: dict, estimate: dict) -> list[Option]:
    validate_rates(rates)
    roles = rates["roles"]
    stages = estimate.get("stages")
    if not isinstance(stages, dict) or not stages:
        raise PricingError("estimate: 'stages' must be a non-empty mapping of stage -> {role: hours}")
    for stage, by_role in stages.items():
        if not isinstance(by_role, dict) or not by_role:
            raise PricingError(f"estimate: stage '{stage}' must map roles to hours")
        for role, hours in by_role.items():
            if role not in roles:
                raise PricingError(f"estimate: stage '{stage}' uses unknown role '{role}'")
            _number(hours, f"estimate: stages.{stage}.{role}")
    buffer = _number(estimate.get("risk_buffer", 0), "estimate: risk_buffer", high=2)
    expenses = estimate.get("expenses") or []
    if not isinstance(expenses, list):
        raise PricingError("estimate: 'expenses' must be a list")
    options = estimate.get("options") or [{"name": "single", "include": list(stages)}]
    markup = _number(rates.get("expense_markup", 0), "rates: expense_markup", high=5)
    target = float(rates["target_margin"])
    step = float(rates.get("rounding", 1))
    priced: list[Option] = []
    for spec in options:
        name = str(spec.get("name") or "").strip()
        if not name:
            raise PricingError("estimate: every option needs a 'name'")
        include = spec.get("include") or list(stages)
        unknown = [stage for stage in include if stage not in stages]
        if unknown:
            raise PricingError(f"estimate: option '{name}' includes unknown stage(s) {unknown}")
        hours_by_role: dict[str, float] = {}
        for stage in include:
            for role, hours in stages[stage].items():
                hours_by_role[role] = hours_by_role.get(role, 0.0) + hours * (1 + buffer)
        hours = sum(hours_by_role.values())
        labour = sum(h * roles[r]["cost_per_hour"] for r, h in hours_by_role.items())
        overhead = labour * float(rates.get("overhead_rate", 0))
        option_expenses = 0.0
        for index, item in enumerate(expenses, start=1):
            if not isinstance(item, dict):
                raise PricingError(f"estimate: expense {index} must be a mapping")
            only = item.get("only")
            if only is None or name in only:
                option_expenses += _number(item.get("cost"), f"estimate: expense {index} cost")
        total_cost = labour + overhead + option_expenses
        rate_price = sum(h * roles[r]["rate_per_hour"] for r, h in hours_by_role.items()) + option_expenses * (1 + markup)
        floor_price = total_cost / (1 - target)
        value_priced = spec.get("price") is not None
        if value_priced:
            price = _number(spec["price"], f"estimate: option '{name}' price", low=0.01)
        else:
            price = round_up(max(rate_price, floor_price), step)
        first = include[0]
        first_stage_cash = option_expenses + sum(
            stages[first][r] * (1 + buffer) * roles[r]["cost_per_hour"]
            for r in stages[first]
            if roles[r].get("external", False)
        )
        priced.append(
            Option(
                name=name,
                label=str(spec.get("label") or name),
                stages=list(include),
                hours=hours,
                labour_cost=labour,
                overhead=overhead,
                expenses=option_expenses,
                total_cost=total_cost,
                rate_price=rate_price,
                floor_price=floor_price,
                price=price,
                value_priced=value_priced,
                gross_margin=(price - total_cost) / price,
                effective_hourly=(price - option_expenses) / hours if hours else 0.0,
                first_stage_cash=first_stage_cash,
                hours_by_role=hours_by_role,
            )
        )
    return priced


def schedule_for(option: Option, rates: dict, estimate: dict) -> list[tuple[str, float, float]]:
    schedule = estimate.get("payment_schedule")
    schedule = validate_schedule(schedule, "estimate: payment_schedule") if schedule else rates["payment_schedule"]
    set_aside = float(rates.get("tax_set_aside", 0))
    return [(str(item["milestone"]), option.price * item["share"], option.price * item["share"] * set_aside) for item in schedule]


def verdict(option: Option, rates: dict, deposit: float) -> tuple[str, list[str]]:
    reasons: list[str] = []
    target, floor = float(rates["target_margin"]), float(rates["floor_margin"])
    if option.gross_margin >= target:
        status = "GO"
    elif option.gross_margin >= floor:
        status = "REVIEW"
        reasons.append(f"margin {option.gross_margin:.0%} is below target {target:.0%} but above floor {floor:.0%}: founder decides")
    else:
        status = "NO-GO"
        reasons.append(f"margin {option.gross_margin:.0%} is below floor {floor:.0%}: rescope or reprice")
    if deposit + 1e-9 < option.first_stage_cash:
        reasons.append("deposit does not cover expenses plus first-stage collaborator cost")
        if status == "GO":
            status = "REVIEW"
    return status, reasons


def fmt(value: float) -> str:
    return f"{value:,.0f}"


def render(rates: dict, estimate: dict, options: list[Option]) -> str:
    unit = str(rates.get("currency_label") or "units")
    lines = [
        f"# Pricing check: {estimate.get('codename', 'unnamed')} ({estimate.get('offer', 'offer not set')})",
        "",
        f"Private output; amounts in {unit}, exclusive of GST. Do not paste into the repository.",
        "",
        "| Option | Stages | Hours | Cost | Floor price | Rate-card price | Price | Gross margin | Effective hourly | Verdict |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    details: list[str] = []
    for option in options:
        schedule = schedule_for(option, rates, estimate)
        status, reasons = verdict(option, rates, schedule[0][1])
        basis = " (value)" if option.value_priced else ""
        lines.append(
            f"| {option.label} | {len(option.stages)} | {option.hours:.1f} | {fmt(option.total_cost)} | "
            f"{fmt(option.floor_price)} | {fmt(option.rate_price)} | {fmt(option.price)}{basis} | "
            f"{option.gross_margin:.0%} | {fmt(option.effective_hourly)} | {status} |"
        )
        details += ["", f"## {option.label}", ""]
        details.append("Hours by role: " + ", ".join(f"{r} {h:.1f}" for r, h in sorted(option.hours_by_role.items())) + ".")
        details.append(
            f"Cost = labour {fmt(option.labour_cost)} + overhead {fmt(option.overhead)} + expenses {fmt(option.expenses)}."
        )
        details += ["", "| Milestone | Amount | Tax set-aside |", "| --- | ---: | ---: |"]
        details += [f"| {m} | {fmt(a)} | {fmt(t)} |" for m, a, t in schedule]
        details.append("")
        details.append(f"Cash check: first payment {fmt(schedule[0][1])} vs expenses plus first-stage collaborator cost {fmt(option.first_stage_cash)}.")
        for reason in reasons:
            details.append(f"- {reason}")
    return "\n".join(lines + details) + "\n"


def _warn_if_in_repo(path: Path) -> None:
    try:
        path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        return
    print(f"warning: {path} is inside the public repository; keep rates and estimates in the vault", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Price an estimate against private vault rates (prints only).")
    parser.add_argument("estimate", type=Path, help="estimate YAML, normally in the vault under <codename>/finance/")
    parser.add_argument("--rates", type=Path, help="rates YAML (default: $THREEW_VAULT/rates.yaml)")
    args = parser.parse_args(argv)
    rates_path = args.rates or vault_dir() / "rates.yaml"
    for path in (rates_path, args.estimate):
        _warn_if_in_repo(path)
    try:
        rates, estimate = load_yaml(rates_path), load_yaml(args.estimate)
        output = render(rates, estimate, price_estimate(rates, estimate))
    except PricingError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
