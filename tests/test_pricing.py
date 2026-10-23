from __future__ import annotations

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import pricing

# Fictional numbers for tests only; not studio rates.
RATES = {
    "currency_label": "units",
    "roles": {
        "founder": {"cost_per_hour": 10, "rate_per_hour": 30},
        "designer": {"cost_per_hour": 8, "rate_per_hour": 20, "external": True},
    },
    "overhead_rate": 0.25,
    "expense_markup": 0.1,
    "target_margin": 0.5,
    "floor_margin": 0.3,
    "tax_set_aside": 0.2,
    "rounding": 50,
    "payment_schedule": [
        {"milestone": "Deposit", "share": 0.5},
        {"milestone": "Final", "share": 0.5},
    ],
}
ESTIMATE = {
    "codename": "stillsoil-atelier",
    "offer": "identity-system",
    "risk_buffer": 0.1,
    "stages": {
        "discover": {"founder": 10, "designer": 10},
        "deliver": {"founder": 10, "designer": 30},
    },
    "expenses": [{"item": "fonts", "cost": 100}, {"item": "stock", "cost": 50, "only": ["better"]}],
    "options": [
        {"name": "good", "include": ["discover"]},
        {"name": "better", "include": ["discover", "deliver"]},
    ],
}


def copy(data: dict) -> dict:
    return yaml.safe_load(yaml.safe_dump(data))


class PriceEstimateTests(unittest.TestCase):
    def test_cost_floor_and_rate_price(self) -> None:
        good, better = pricing.price_estimate(copy(RATES), copy(ESTIMATE))
        self.assertAlmostEqual(good.hours, 22.0)
        self.assertAlmostEqual(good.labour_cost, 11 * 10 + 11 * 8)
        self.assertAlmostEqual(good.overhead, 198 * 0.25)
        self.assertAlmostEqual(good.total_cost, 198 + 49.5 + 100)
        self.assertAlmostEqual(good.floor_price, 347.5 / 0.5)
        self.assertAlmostEqual(good.rate_price, 11 * 30 + 11 * 20 + 110)
        self.assertEqual(good.price, 700.0)  # max(660, 695) rounded up to 50
        self.assertAlmostEqual(good.gross_margin, (700 - 347.5) / 700)
        self.assertAlmostEqual(good.effective_hourly, 600 / 22)
        self.assertAlmostEqual(better.expenses, 150)

    def test_value_price_overrides_and_can_fail_margin(self) -> None:
        estimate = copy(ESTIMATE)
        estimate["options"][0]["price"] = 400
        good = pricing.price_estimate(copy(RATES), estimate)[0]
        self.assertTrue(good.value_priced)
        self.assertEqual(good.price, 400)
        status, reasons = pricing.verdict(good, pricing.validate_rates(copy(RATES)), deposit=200)
        self.assertEqual(status, "NO-GO")
        self.assertIn("below floor", reasons[0])

    def test_verdict_bands_and_cash_check(self) -> None:
        rates = pricing.validate_rates(copy(RATES))
        good = pricing.price_estimate(copy(RATES), copy(ESTIMATE))[0]
        self.assertEqual(pricing.verdict(good, rates, deposit=350)[0], "GO")
        # The first stage needs expenses plus external designer cost: 100 + 11 * 8.
        self.assertAlmostEqual(good.first_stage_cash, 188)
        status, reasons = pricing.verdict(good, rates, deposit=100)
        self.assertEqual(status, "REVIEW")
        self.assertIn("deposit", reasons[0])
        good.gross_margin = 0.4
        self.assertEqual(pricing.verdict(good, rates, deposit=350)[0], "REVIEW")

    def test_schedule_and_tax_set_aside(self) -> None:
        good = pricing.price_estimate(copy(RATES), copy(ESTIMATE))[0]
        schedule = pricing.schedule_for(good, copy(RATES), copy(ESTIMATE))
        self.assertEqual(schedule, [("Deposit", 350.0, 70.0), ("Final", 350.0, 70.0)])

    def test_rejects_bad_inputs(self) -> None:
        cases = [
            ({"payment_schedule": [{"milestone": "Deposit", "share": 0.4}]}, {}, "sum to 1"),
            ({"target_margin": 1.2}, {}, "target_margin"),
            ({}, {"stages": {"discover": {"intern": 5}}}, "unknown role"),
            ({}, {"options": [{"name": "x", "include": ["missing"]}]}, "unknown stage"),
            ({}, {"risk_buffer": "high"}, "risk_buffer"),
        ]
        for rates_patch, estimate_patch, message in cases:
            with self.subTest(message=message):
                rates, estimate = copy(RATES), copy(ESTIMATE)
                rates.update(rates_patch)
                estimate.update(estimate_patch)
                with self.assertRaisesRegex(pricing.PricingError, message):
                    pricing.price_estimate(rates, estimate)


class CliTests(unittest.TestCase):
    def test_reads_rates_from_vault_and_prints_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            vault = Path(temp)
            (vault / "rates.yaml").write_text(yaml.safe_dump(RATES), encoding="utf-8")
            estimate = vault / "estimate.yaml"
            estimate.write_text(yaml.safe_dump(ESTIMATE), encoding="utf-8")
            before = sorted(p.name for p in vault.iterdir())
            out = io.StringIO()
            with patch.dict(os.environ, {"THREEW_VAULT": temp}), redirect_stdout(out):
                self.assertEqual(pricing.main([str(estimate)]), 0)
            self.assertEqual(sorted(p.name for p in vault.iterdir()), before)
        text = out.getvalue()
        self.assertIn("# Pricing check: stillsoil-atelier", text)
        self.assertIn("| Deposit | 350 | 70 |", text)
        self.assertIn("GO", text)

    def test_missing_rates_is_an_error(self) -> None:
        err = io.StringIO()
        with redirect_stderr(err):
            self.assertEqual(pricing.main(["/nonexistent/estimate.yaml", "--rates", "/nonexistent/rates.yaml"]), 2)
        self.assertIn("file not found", err.getvalue())


if __name__ == "__main__":
    unittest.main()
