#!/usr/bin/env python3
"""WCAG contrast and CIEDE2000 palette checks for 3RDWRONG.

Run with ``uv run python scripts/colour_check.py --help``. All calculations
are local and use only the Python standard library. WCAG 2.2 contrast supplies
the contrast pass/fail rules; CIEDE2000 and CVD simulations screen palette
differences against a project-declared threshold.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections.abc import Sequence
from typing import Any


class ColourCheckError(ValueError):
    """Invalid colour or check parameters supplied to the tool."""


_RGB = tuple[int, int, int]
_LAB = tuple[float, float, float]
_MATRIX = tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]
_HEX_RE = re.compile(r"^(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")

# Machado, Oliveira & Fernandes (2009), full-severity linear-sRGB simulation
# matrices. The complete severity ladder is embedded below and interpolated
# between adjacent published 0.1 steps for values between them.
# Source: https://profs.ic.uff.br/~laffernandes/content/publications/journal/2009_tvcg_15%286%29/machado_oliveira_fernandes-tvcg-15%286%29-2009-corrected.pdf
# Cross-check of the tabulated coefficients: https://github.com/colour-science/colour/blob/develop/colour/blindness/datasets/machado2010.py
MACHADO_MATRICES: dict[str, dict[float, _MATRIX]] = {
    'protan': {
        0.0: ((1.000000, 0.000000, -0.000000), (0.000000, 1.000000, 0.000000), (-0.000000, -0.000000, 1.000000)),
        0.1: ((0.856167, 0.182038, -0.038205), (0.029342, 0.955115, 0.015544), (-0.002880, -0.001563, 1.004443)),
        0.2: ((0.734766, 0.334872, -0.069637), (0.051840, 0.919198, 0.028963), (-0.004928, -0.004209, 1.009137)),
        0.3: ((0.630323, 0.465641, -0.095964), (0.069181, 0.890046, 0.040773), (-0.006308, -0.007724, 1.014032)),
        0.4: ((0.539009, 0.579343, -0.118352), (0.082546, 0.866121, 0.051332), (-0.007136, -0.011959, 1.019095)),
        0.5: ((0.458064, 0.679578, -0.137642), (0.092785, 0.846313, 0.060902), (-0.007494, -0.016807, 1.024301)),
        0.6: ((0.385450, 0.769005, -0.154455), (0.100526, 0.829802, 0.069673), (-0.007442, -0.022190, 1.029632)),
        0.7: ((0.319627, 0.849633, -0.169261), (0.106241, 0.815969, 0.077790), (-0.007025, -0.028051, 1.035076)),
        0.8: ((0.259411, 0.923008, -0.182420), (0.110296, 0.804340, 0.085364), (-0.006276, -0.034346, 1.040622)),
        0.9: ((0.203876, 0.990338, -0.194214), (0.112975, 0.794542, 0.092483), (-0.005222, -0.041043, 1.046265)),
        1.0: ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
    },
    'deutan': {
        0.0: ((1.000000, 0.000000, -0.000000), (0.000000, 1.000000, 0.000000), (-0.000000, -0.000000, 1.000000)),
        0.1: ((0.866435, 0.177704, -0.044139), (0.049567, 0.939063, 0.011370), (-0.003453, 0.007233, 0.996220)),
        0.2: ((0.760729, 0.319078, -0.079807), (0.090568, 0.889315, 0.020117), (-0.006027, 0.013325, 0.992702)),
        0.3: ((0.675425, 0.433850, -0.109275), (0.125303, 0.847755, 0.026942), (-0.007950, 0.018572, 0.989378)),
        0.4: ((0.605511, 0.528560, -0.134071), (0.155318, 0.812366, 0.032316), (-0.009376, 0.023176, 0.986200)),
        0.5: ((0.547494, 0.607765, -0.155259), (0.181692, 0.781742, 0.036566), (-0.010410, 0.027275, 0.983136)),
        0.6: ((0.498864, 0.674741, -0.173604), (0.205199, 0.754872, 0.039929), (-0.011131, 0.030969, 0.980162)),
        0.7: ((0.457771, 0.731899, -0.189670), (0.226409, 0.731012, 0.042579), (-0.011595, 0.034333, 0.977261)),
        0.8: ((0.422823, 0.781057, -0.203881), (0.245752, 0.709602, 0.044646), (-0.011843, 0.037423, 0.974421)),
        0.9: ((0.392952, 0.823610, -0.216562), (0.263559, 0.690210, 0.046232), (-0.011910, 0.040281, 0.971630)),
        1.0: ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.011820, 0.042940, 0.968881)),
    },
    'tritan': {
        0.0: ((1.000000, 0.000000, -0.000000), (0.000000, 1.000000, 0.000000), (-0.000000, -0.000000, 1.000000)),
        0.1: ((0.926670, 0.092514, -0.019184), (0.021191, 0.964503, 0.014306), (0.008437, 0.054813, 0.936750)),
        0.2: ((0.895720, 0.133330, -0.029050), (0.029997, 0.945400, 0.024603), (0.013027, 0.104707, 0.882266)),
        0.3: ((0.905871, 0.127791, -0.033662), (0.026856, 0.941251, 0.031893), (0.013410, 0.148296, 0.838294)),
        0.4: ((0.948035, 0.089490, -0.037526), (0.014364, 0.946792, 0.038844), (0.010853, 0.193991, 0.795156)),
        0.5: ((1.017277, 0.027029, -0.044306), (-0.006113, 0.958479, 0.047634), (0.006379, 0.248708, 0.744913)),
        0.6: ((1.104996, -0.046633, -0.058363), (-0.032137, 0.971635, 0.060503), (0.001336, 0.317922, 0.680742)),
        0.7: ((1.193214, -0.109812, -0.083402), (-0.058496, 0.979410, 0.079086), (-0.002346, 0.403492, 0.598854)),
        0.8: ((1.257728, -0.139648, -0.118081), (-0.078003, 0.975409, 0.102594), (-0.003316, 0.501214, 0.502102)),
        0.9: ((1.278864, -0.125333, -0.153531), (-0.084748, 0.957674, 0.127074), (-0.000989, 0.601151, 0.399838)),
        1.0: ((1.255528, -0.076749, -0.178779), (-0.078411, 0.930809, 0.147602), (0.004733, 0.691367, 0.303900)),
    },
}


# ---------------------------------------------------------------------------
# sRGB and WCAG 2.2 contrast


def parse_hex(value: str) -> _RGB:
    """Parse 3- or 6-digit sRGB hex; alpha is deliberately unsupported."""
    if not isinstance(value, str):
        raise ColourCheckError("colour must be a 3- or 6-digit sRGB hex string")
    raw = value.strip().removeprefix("#")
    if not _HEX_RE.fullmatch(raw):
        raise ColourCheckError(f"invalid sRGB hex colour: {value!r}")
    if len(raw) == 3:
        raw = "".join(char * 2 for char in raw)
    return tuple(int(raw[index:index + 2], 16) for index in (0, 2, 4))  # type: ignore[return-value]


def format_hex(rgb: Sequence[int]) -> str:
    """Format integer RGB channels as uppercase ``#RRGGBB``."""
    channels = _parse_rgb(rgb)
    return "#" + "".join(f"{channel:02X}" for channel in channels)


def _parse_rgb(colour: str | Sequence[int]) -> _RGB:
    if isinstance(colour, str):
        return parse_hex(colour)
    if isinstance(colour, (bytes, bytearray)) or not isinstance(colour, Sequence) or len(colour) != 3:
        raise ColourCheckError("RGB colour must contain exactly three integer channels")
    channels: list[int] = []
    for channel in colour:
        if isinstance(channel, bool) or not isinstance(channel, int) or not 0 <= channel <= 255:
            raise ColourCheckError("RGB channels must be integers from 0 through 255")
        channels.append(channel)
    return channels[0], channels[1], channels[2]


def srgb_to_linear(channel: float) -> float:
    """Decode one normalized sRGB channel using WCAG 2.2's 0.04045 breakpoint."""
    if not math.isfinite(channel) or not 0.0 <= channel <= 1.0:
        raise ColourCheckError("normalized sRGB channels must be finite values from 0 through 1")
    if channel <= 0.04045:
        return channel / 12.92
    return ((channel + 0.055) / 1.055) ** 2.4


def _linear_rgb(colour: str | Sequence[int]) -> tuple[float, float, float]:
    return tuple(srgb_to_linear(channel / 255.0) for channel in _parse_rgb(colour))  # type: ignore[return-value]


def relative_luminance(colour: str | Sequence[int]) -> float:
    """Calculate WCAG 2.2 relative luminance for opaque sRGB."""
    red, green, blue = _linear_rgb(colour)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(foreground: str | Sequence[int], background: str | Sequence[int]) -> float:
    """Return the WCAG 2.2 contrast ratio for opaque sRGB foreground/background."""
    first = relative_luminance(foreground)
    second = relative_luminance(background)
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def wcag_passes(ratio: float) -> dict[str, bool]:
    """Return WCAG AA/AAA outcomes for normal and large text."""
    if not math.isfinite(ratio) or ratio < 1.0:
        raise ColourCheckError("contrast ratio must be finite and at least 1")
    return {
        "aa_normal": ratio >= 4.5,
        "aaa_normal": ratio >= 7.0,
        "aa_large": ratio >= 3.0,
        "aaa_large": ratio >= 4.5,
    }


def is_large_text(font_size_pt: float, bold: bool = False) -> bool:
    """WCAG large-scale text: at least 18 pt, or at least 14 pt and bold."""
    if not isinstance(font_size_pt, (int, float)) or isinstance(font_size_pt, bool) or not math.isfinite(font_size_pt):
        raise ColourCheckError("font size must be a finite point value")
    return font_size_pt >= 18.0 or (font_size_pt >= 14.0 and bool(bold))


def contrast_report(foreground: str, background: str) -> dict[str, Any]:
    foreground_hex = format_hex(parse_hex(foreground))
    background_hex = format_hex(parse_hex(background))
    ratio = contrast_ratio(foreground_hex, background_hex)
    return {
        "foreground": foreground_hex,
        "background": background_hex,
        "wcag_contrast_ratio": ratio,
        "wcag": wcag_passes(ratio),
    }


# ---------------------------------------------------------------------------
# CVD simulation and greyscale




def cvd_matrix(kind: str, severity: float = 1.0) -> _MATRIX:
    """Return an interpolated Machado et al. linear-sRGB matrix (severity 0–1)."""
    aliases = {
        "protan": "protan",
        "protanopia": "protan",
        "protanomaly": "protan",
        "deutan": "deutan",
        "deuteranopia": "deutan",
        "deuteranomaly": "deutan",
        "tritan": "tritan",
        "tritanopia": "tritan",
        "tritanomaly": "tritan",
    }
    key = aliases.get(str(kind).lower())
    if key is None:
        raise ColourCheckError("CVD kind must be protan, deutan, or tritan")
    if isinstance(severity, bool) or not isinstance(severity, (int, float)) or not math.isfinite(severity) or not 0.0 <= severity <= 1.0:
        raise ColourCheckError("CVD severity must be a finite number from 0 through 1")
    severity = float(severity)
    matrices = MACHADO_MATRICES[key]
    nearest = round(severity * 10) / 10
    if math.isclose(severity, nearest, abs_tol=1e-12):
        return matrices[nearest]
    lower = math.floor(severity * 10) / 10
    upper = math.ceil(severity * 10) / 10
    weight = (severity - lower) / (upper - lower)
    return tuple(
        tuple(matrices[lower][row][column] * (1.0 - weight) + matrices[upper][row][column] * weight for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def _linear_to_srgb(channel: float) -> float:
    channel = min(1.0, max(0.0, channel))
    if channel <= 0.0031308:
        return 12.92 * channel
    return 1.055 * channel ** (1.0 / 2.4) - 0.055


def simulate_cvd(colour: str, kind: str, severity: float = 1.0) -> str:
    """Apply Machado simulation in linear RGB and return clipped sRGB hex."""
    matrix = cvd_matrix(kind, severity)
    red, green, blue = _linear_rgb(colour)
    linear = (red, green, blue)
    simulated = tuple(sum(matrix[row][column] * linear[column] for column in range(3)) for row in range(3))
    encoded = tuple(int(math.floor(_linear_to_srgb(channel) * 255.0 + 0.5)) for channel in simulated)
    return format_hex(encoded)


def grayscale(colour: str | Sequence[int]) -> str:
    """Return an sRGB grey whose WCAG relative luminance matches the source."""
    luminance = relative_luminance(colour)
    encoded = _linear_to_srgb(luminance)
    level = int(math.floor(encoded * 255.0 + 0.5))
    return format_hex((level, level, level))


# ---------------------------------------------------------------------------
# CIELAB and CIEDE2000


def rgb_to_lab(colour: str | Sequence[int]) -> _LAB:
    """Convert opaque sRGB into CIELAB relative to the D65 sRGB white point."""
    red, green, blue = _linear_rgb(colour)
    x = (0.4124564 * red + 0.3575761 * green + 0.1804375 * blue) / 0.95047
    y = 0.2126729 * red + 0.7151522 * green + 0.0721750 * blue
    z = (0.0193339 * red + 0.1191920 * green + 0.9503041 * blue) / 1.08883
    delta = 6.0 / 29.0
    delta_cubed = delta ** 3
    slope = 1.0 / (3.0 * delta ** 2)

    def f(value: float) -> float:
        return value ** (1.0 / 3.0) if value > delta_cubed else slope * value + 4.0 / 29.0

    fx, fy, fz = f(x), f(y), f(z)
    return 116.0 * fy - 16.0, 500.0 * (fx - fy), 200.0 * (fy - fz)


def ciede2000(lab1: Sequence[float], lab2: Sequence[float]) -> float:
    """Calculate CIEDE2000 ΔE00 (kL = kC = kH = 1) for two CIELAB triples."""
    if len(lab1) != 3 or len(lab2) != 3:
        raise ColourCheckError("CIEDE2000 inputs must each contain L*, a*, b*")
    if not all(math.isfinite(float(value)) for value in (*lab1, *lab2)):
        raise ColourCheckError("CIEDE2000 inputs must be finite")
    l1, a1, b1 = (float(value) for value in lab1)
    l2, a2, b2 = (float(value) for value in lab2)
    c1 = math.hypot(a1, b1)
    c2 = math.hypot(a2, b2)
    c_bar = (c1 + c2) / 2.0
    c_bar_7 = c_bar ** 7
    g = 0.5 * (1.0 - math.sqrt(c_bar_7 / (c_bar_7 + 25.0 ** 7))) if c_bar else 0.5
    a1p = (1.0 + g) * a1
    a2p = (1.0 + g) * a2
    c1p = math.hypot(a1p, b1)
    c2p = math.hypot(a2p, b2)

    def hue(a: float, b: float) -> float:
        if a == 0.0 and b == 0.0:
            return 0.0
        return math.degrees(math.atan2(b, a)) % 360.0

    h1p = hue(a1p, b1)
    h2p = hue(a2p, b2)
    delta_l = l2 - l1
    delta_c = c2p - c1p
    if c1p * c2p == 0.0:
        delta_h_angle = 0.0
    else:
        delta_h_angle = h2p - h1p
        if delta_h_angle > 180.0:
            delta_h_angle -= 360.0
        elif delta_h_angle < -180.0:
            delta_h_angle += 360.0
    delta_h = 2.0 * math.sqrt(c1p * c2p) * math.sin(math.radians(delta_h_angle / 2.0))
    l_bar = (l1 + l2) / 2.0
    c_bar_p = (c1p + c2p) / 2.0
    if c1p * c2p == 0.0:
        h_bar = h1p + h2p
    elif abs(h1p - h2p) <= 180.0:
        h_bar = (h1p + h2p) / 2.0
    elif h1p + h2p < 360.0:
        h_bar = (h1p + h2p + 360.0) / 2.0
    else:
        h_bar = (h1p + h2p - 360.0) / 2.0
    t = (
        1.0
        - 0.17 * math.cos(math.radians(h_bar - 30.0))
        + 0.24 * math.cos(math.radians(2.0 * h_bar))
        + 0.32 * math.cos(math.radians(3.0 * h_bar + 6.0))
        - 0.20 * math.cos(math.radians(4.0 * h_bar - 63.0))
    )
    l_offset = l_bar - 50.0
    s_l = 1.0 + 0.015 * l_offset ** 2 / math.sqrt(20.0 + l_offset ** 2)
    s_c = 1.0 + 0.045 * c_bar_p
    s_h = 1.0 + 0.015 * c_bar_p * t
    c_bar_p_7 = c_bar_p ** 7
    r_c = 2.0 * math.sqrt(c_bar_p_7 / (c_bar_p_7 + 25.0 ** 7)) if c_bar_p else 0.0
    delta_theta = 30.0 * math.exp(-((h_bar - 275.0) / 25.0) ** 2)
    r_t = -math.sin(math.radians(2.0 * delta_theta)) * r_c
    l_term, c_term, h_term = delta_l / s_l, delta_c / s_c, delta_h / s_h
    return math.sqrt(max(0.0, l_term ** 2 + c_term ** 2 + h_term ** 2 + r_t * c_term * h_term))


# ---------------------------------------------------------------------------
# Palette analysis and output


def _parse_text_pairs(value: str | Sequence[tuple[str, str]]) -> list[tuple[str, str]]:
    if not isinstance(value, str):
        result = []
        for foreground, background in value:
            result.append((format_hex(parse_hex(foreground)), format_hex(parse_hex(background))))
        return result
    if not value.strip():
        return []
    result = []
    for item in value.split(","):
        if item.count(":") != 1:
            raise ColourCheckError(f"text pair must use foreground:background syntax: {item!r}")
        foreground, background = item.split(":", 1)
        result.append((format_hex(parse_hex(foreground.strip())), format_hex(parse_hex(background.strip()))))
    return result


def _vision_views(colors: list[str], severity: float) -> tuple[dict[str, list[str]], dict[str, str]]:
    if severity == 1.0:
        labels = {
            "normal": "Normal vision",
            "protanopia": "Protanopia",
            "deuteranopia": "Deuteranopia",
            "tritanopia": "Tritanopia",
            "greyscale": "Greyscale (WCAG relative luminance)",
        }
    else:
        labels = {
            "normal": "Normal vision",
            "protanopia": f"Protan anomaly (Machado severity {severity:g})",
            "deuteranopia": f"Deuteranomaly (Machado severity {severity:g})",
            "tritanopia": f"Tritanomaly (Machado severity {severity:g})",
            "greyscale": "Greyscale (WCAG relative luminance)",
        }
    views = {
        "normal": colors,
        "protanopia": [simulate_cvd(color, "protan", severity) for color in colors],
        "deuteranopia": [simulate_cvd(color, "deutan", severity) for color in colors],
        "tritanopia": [simulate_cvd(color, "tritan", severity) for color in colors],
        "greyscale": [grayscale(color) for color in colors],
    }
    return views, labels


def palette_report(
    colors: Sequence[str],
    min_delta_e: float,
    text_pairs: str | Sequence[tuple[str, str]] = (),
    severity: float = 1.0,
) -> dict[str, Any]:
    """Analyze all palette pairs; the caller must declare a ΔE00 cutoff."""
    if isinstance(min_delta_e, bool) or not isinstance(min_delta_e, (int, float)) or not math.isfinite(min_delta_e) or min_delta_e < 0:
        raise ColourCheckError("min_delta_e must be a finite non-negative number")
    if len(colors) < 2:
        raise ColourCheckError("palette requires at least two hex colours")
    canonical = [format_hex(parse_hex(color)) for color in colors]
    if isinstance(severity, bool) or not isinstance(severity, (int, float)) or not math.isfinite(severity) or not 0.0 <= severity <= 1.0:
        raise ColourCheckError("CVD severity must be a finite number from 0 through 1")
    declared_pairs = _parse_text_pairs(text_pairs)
    views, labels = _vision_views(canonical, float(severity))
    matrices: dict[str, dict[str, Any]] = {}
    flagged: list[dict[str, Any]] = []
    for mode, shown in views.items():
        labs = [rgb_to_lab(color) for color in shown]
        values = [[0.0 for _ in shown] for _ in shown]
        for left in range(len(shown)):
            for right in range(left + 1, len(shown)):
                delta = ciede2000(labs[left], labs[right])
                values[left][right] = values[right][left] = delta
                if delta < min_delta_e:
                    flagged.append({
                        "mode": mode,
                        "mode_label": labels[mode],
                        "color_1": canonical[left],
                        "color_2": canonical[right],
                        "delta_e_00": delta,
                    })
        matrices[mode] = {"label": labels[mode], "colors": shown, "values": values}
    contrast_pairs = [contrast_report(foreground, background) for foreground, background in declared_pairs]
    return {
        "metric": "CIEDE2000 ΔE00",
        "min_delta_e": float(min_delta_e),
        "flag_rule": "flag when ΔE00 is strictly below the declared threshold",
        "cvd_model": "Machado, Oliveira & Fernandes (2009) precomputed linear-RGB matrices; adjacent 0.1 severities are linearly interpolated",
        "cvd_severity": float(severity),
        "colors": canonical,
        "delta_e_matrices": matrices,
        "flagged_pairs": flagged,
        "contrast_pairs": contrast_pairs,
        "lab_white_point": "D65 (sRGB)",
    }


def _format_pass(value: bool) -> str:
    return "Pass" if value else "Fail"


def render_contrast_markdown(result: dict[str, Any]) -> str:
    return "\n".join([
        "# Colour contrast check",
        "",
        f"Foreground `{result['foreground']}` on background `{result['background']}`.",
        "",
        f"WCAG 2.2 contrast: **{result['wcag_contrast_ratio']:.2f}:1** (unrounded value used for thresholds).",
        "",
        "| Text category | Minimum | Result |",
        "| --- | ---: | --- |",
        f"| AA normal | 4.5:1 | {_format_pass(result['wcag']['aa_normal'])} |",
        f"| AAA normal | 7:1 | {_format_pass(result['wcag']['aaa_normal'])} |",
        f"| AA large | 3:1 | {_format_pass(result['wcag']['aa_large'])} |",
        f"| AAA large | 4.5:1 | {_format_pass(result['wcag']['aaa_large'])} |",
        "",
        "Large text follows WCAG: at least 18 pt, or at least 14 pt when bold. This calculation does not itself establish conformance.",
        "",
    ])


def render_palette_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Colour palette check",
        "",
        f"Metric: **{report['metric']}**; declared cutoff: **ΔE00 < {report['min_delta_e']:g}** (strictly below is flagged).",
        f"CVD model: {report['cvd_model']}; severity: **{report['cvd_severity']:g}**. At 1.0 the modes are dichromacy; lower severities use the published anomaly matrices.",
        f"CIELAB reference white: {report['lab_white_point']}.",
        "",
    ]
    if report["contrast_pairs"]:
        lines.extend([
            "## Declared text pairings",
            "",
            "| Foreground / background | WCAG ratio | AA normal | AAA normal | AA large | AAA large |",
            "| --- | ---: | --- | --- | --- | --- |",
        ])
        for pair in report["contrast_pairs"]:
            checks = pair["wcag"]
            lines.append(
                f"| `{pair['foreground']}` / `{pair['background']}` | {pair['wcag_contrast_ratio']:.2f}:1 | "
                f"{_format_pass(checks['aa_normal'])} | {_format_pass(checks['aaa_normal'])} | "
                f"{_format_pass(checks['aa_large'])} | {_format_pass(checks['aaa_large'])} | "
            )
        lines.extend(["", "WCAG 2.2 contrast determines pass/fail. Large text is at least 18 pt, or at least 14 pt bold.", ""])
    for mode, matrix in report["delta_e_matrices"].items():
        lines.extend([f"## ΔE00 matrix — {matrix['label']}", "", "| Colour | " + " | ".join(f"`{color}`" for color in report["colors"]) + " |", "| --- | " + " ---: |" * len(report["colors"])])
        for index, color in enumerate(report["colors"]):
            lines.append(f"| `{color}` | " + " | ".join(f"{value:.2f}" for value in matrix["values"][index]) + " |")
        lines.append("")
    lines.extend(["## Flagged pairs", ""])
    if report["flagged_pairs"]:
        lines.extend([
            "| Vision mode | Pair | ΔE00 |",
            "| --- | --- | ---: |",
        ])
        for item in report["flagged_pairs"]:
            lines.append(f"| {item['mode_label']} | `{item['color_1']}` / `{item['color_2']}` | {item['delta_e_00']:.2f} |")
    else:
        lines.append("No pair fell below the declared threshold in any view.")
    lines.extend(["", "CVD simulations and ΔE00 flags are screening aids, not a user test or a conformance result.", ""])
    return "\n".join(lines)


def _finite_nonnegative(value: str) -> float:
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a number") from None
    if not math.isfinite(number) or number < 0.0:
        raise argparse.ArgumentTypeError("must be a finite non-negative number")
    return number


def _severity_value(value: str) -> float:
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a number from 0 through 1") from None
    if not math.isfinite(number) or not 0.0 <= number <= 1.0:
        raise argparse.ArgumentTypeError("must be a finite number from 0 through 1")
    return number


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check sRGB text contrast and palette distinguishability.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    contrast_parser = subparsers.add_parser("contrast", help="compute WCAG 2.2 contrast for one text pair")
    contrast_parser.add_argument("foreground", help="text foreground sRGB hex")
    contrast_parser.add_argument("background", help="background sRGB hex")
    contrast_parser.add_argument("--format", choices=("md", "json"), default="md")
    palette_parser = subparsers.add_parser("palette", help="compare all palette pairs under vision simulations")
    palette_parser.add_argument("colors", nargs="+", help="palette colours as sRGB hex values")
    palette_parser.add_argument("--min-delta-e", required=True, type=_finite_nonnegative, help="required CIEDE2000 ΔE00 flag cutoff")
    palette_parser.add_argument("--text-pairs", default="", help="comma-separated foreground:background hex pairs")
    palette_parser.add_argument("--cvd-severity", type=_severity_value, default=1.0, help="Machado severity from 0 through 1 (default: 1.0)")
    palette_parser.add_argument("--format", choices=("md", "json"), default="md")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "contrast":
            result = contrast_report(args.foreground, args.background)
            output = json.dumps(result, indent=2) if args.format == "json" else render_contrast_markdown(result)
        else:
            result = palette_report(args.colors, args.min_delta_e, args.text_pairs, args.cvd_severity)
            output = json.dumps(result, indent=2) if args.format == "json" else render_palette_markdown(result)
    except ColourCheckError as exc:
        parser.error(str(exc))
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
