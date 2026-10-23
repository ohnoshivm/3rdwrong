"""Published-vector tests for scripts/colour_check.py.

Reference sources:
- WCAG 2.2 luminance, 0.04045 transfer threshold, and contrast definition:
  https://www.w3.org/TR/WCAG22/#dfn-relative-luminance
  https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
- WebAIM's contrast checker API reports #767676/#FFFFFF as 4.54:1 and
  #777777/#FFFFFF as 4.47:1 (the tool's displayed ratio):
  https://webaim.org/resources/contrastchecker/?fcolor=767676&bcolor=FFFFFF&api
  https://webaim.org/resources/contrastchecker/?fcolor=777777&bcolor=FFFFFF&api
  Black on white is 21:1 in HHS's contrast reference: https://www.hhs.gov/sites/default/files/os-a11y-color-contrast-reference.pdf
- CIEDE2000 values are from Sharma, Wu & Dalal's supplementary published data:
  https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/dataNprograms/ciede2000testdata.txt
  Paper: https://doi.org/10.1002/col.20070
- Machado severity-1 matrices are published in Machado, Oliveira & Fernandes
  (2009), IEEE TVCG 15(6), 1291-1298, and reproduced by Colour Science:
  https://profs.ic.uff.br/~laffernandes/content/publications/journal/2009_tvcg_15%286%29/machado_oliveira_fernandes-tvcg-15%286%29-2009-corrected.pdf
  https://github.com/colour-science/colour/blob/develop/colour/blindness/datasets/machado2010.py
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import colour_check


class HexAndContrastTests(unittest.TestCase):
    def test_parses_shorthand_and_full_srgb_hex(self) -> None:
        self.assertEqual(colour_check.parse_hex("#767"), (119, 102, 119))
        self.assertEqual(colour_check.parse_hex("767676"), (118, 118, 118))
        self.assertEqual(colour_check.parse_hex("#AbC123"), (171, 193, 35))

    def test_rejects_alpha_and_malformed_hex(self) -> None:
        for invalid in ("#12", "#1234", "#12345678", "red", "#gggggg"):
            with self.subTest(invalid=invalid), self.assertRaises(colour_check.ColourCheckError):
                colour_check.parse_hex(invalid)

    def test_uses_wcag_22_srgb_transfer_breakpoint(self) -> None:
        self.assertAlmostEqual(colour_check.srgb_to_linear(0.04045), 0.04045 / 12.92, places=12)
        self.assertAlmostEqual(
            colour_check.srgb_to_linear(0.0404501),
            ((0.0404501 + 0.055) / 1.055) ** 2.4,
            places=12,
        )

    def test_wcag_reference_pairs_match_published_checker_rounding(self) -> None:
        # WebAIM reports 4.54:1 for #767676; its API renders the #777777
        # ratio as 4.47, while the unrounded WCAG calculation is 4.478089... .
        self.assertAlmostEqual(colour_check.contrast_ratio("#767676", "#ffffff"), 4.54, places=2)
        self.assertLess(colour_check.contrast_ratio("#777777", "#ffffff"), 4.5)
        self.assertEqual(colour_check.contrast_ratio("#000000", "#ffffff"), 21.0)

    def test_wcag_aa_aaa_pass_bands_for_normal_and_large_text(self) -> None:
        passes = colour_check.wcag_passes(colour_check.contrast_ratio("#767676", "#fff"))
        self.assertEqual(passes, {
            "aa_normal": True,
            "aaa_normal": False,
            "aa_large": True,
            "aaa_large": True,
        })
        self.assertTrue(colour_check.is_large_text(18))
        self.assertTrue(colour_check.is_large_text(14, bold=True))
        self.assertFalse(colour_check.is_large_text(17.99))
        self.assertFalse(colour_check.is_large_text(14, bold=False))

class PerceptualDifferenceTests(unittest.TestCase):
    def test_ciede2000_matches_sharma_supplementary_test_vector(self) -> None:
        actual = colour_check.ciede2000((50.0000, 2.6772, -79.7751), (50.0000, 0.0000, -82.7485))
        self.assertAlmostEqual(actual, 2.0425, places=4)

    def test_published_machado_dichromacy_matrices_and_severity_bounds(self) -> None:
        expected = {
            "protan": (
                (0.152286, 1.052583, -0.204868),
                (0.114503, 0.786281, 0.099216),
                (-0.003882, -0.048116, 1.051998),
            ),
            "deutan": (
                (0.367322, 0.860646, -0.227968),
                (0.280085, 0.672501, 0.047413),
                (-0.011820, 0.042940, 0.968881),
            ),
            "tritan": (
                (1.255528, -0.076749, -0.178779),
                (-0.078411, 0.930809, 0.147602),
                (0.004733, 0.691367, 0.303900),
            ),
        }
        for kind, matrix in expected.items():
            with self.subTest(kind=kind):
                actual = colour_check.cvd_matrix(kind, 1.0)
                for actual_row, expected_row in zip(actual, matrix):
                    for actual_value, expected_value in zip(actual_row, expected_row):
                        self.assertAlmostEqual(actual_value, expected_value, places=6)
                self.assertEqual(colour_check.cvd_matrix(kind, 0.0), (
                    (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0),
                ))
                self.assertEqual(colour_check.simulate_cvd("#fff", kind, 1.0), "#FFFFFF")
        self.assertEqual(colour_check.cvd_matrix("protan", 0.5)[0], (0.458064, 0.679578, -0.137642))
        with self.assertRaises(colour_check.ColourCheckError):
            colour_check.cvd_matrix("protan", 1.1)

    def test_grayscale_preserves_luminance_and_sets_equal_channels(self) -> None:
        gray = colour_check.parse_hex(colour_check.grayscale("#a4553a"))
        self.assertEqual(gray[0], gray[1])
        self.assertEqual(gray[1], gray[2])
        self.assertAlmostEqual(
            colour_check.relative_luminance(gray),
            colour_check.relative_luminance("#a4553a"),
            delta=0.004,
        )

    def test_palette_reports_symmetrical_matrices_and_only_subthreshold_flags(self) -> None:
        report = colour_check.palette_report(["#000000", "#ffffff", "#000000"], min_delta_e=2.0)
        self.assertEqual(set(report["delta_e_matrices"]), {
            "normal", "protanopia", "deuteranopia", "tritanopia", "greyscale",
        })
        normal = report["delta_e_matrices"]["normal"]["values"]
        self.assertEqual(normal[0][0], 0.0)
        self.assertEqual(normal[0][1], normal[1][0])
        flagged = {(item["mode"], item["color_1"], item["color_2"]) for item in report["flagged_pairs"]}
        self.assertIn(("normal", "#000000", "#000000"), flagged)
        self.assertTrue(all(item["delta_e_00"] < 2.0 for item in report["flagged_pairs"]))


class CliTests(unittest.TestCase):
    def test_palette_requires_an_explicit_min_delta_e(self) -> None:
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as raised:
            colour_check.main(["palette", "#000", "#fff"])
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("--min-delta-e", stderr.getvalue())

    def test_palette_json_includes_declared_text_pair_wcag(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = colour_check.main([
                "palette", "#000", "#fff", "--min-delta-e", "5",
                "--text-pairs", "#888:#fff", "--format", "json",
            ])
        report = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(len(report["contrast_pairs"]), 1)
        self.assertEqual(report["contrast_pairs"][0]["wcag"]["aa_normal"], False)

    def test_contrast_command_reports_all_four_wcag_text_categories(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = colour_check.main(["contrast", "#767676", "#fff", "--format", "json"])
        result = json.loads(stdout.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(result["wcag"]["aa_normal"], True)
        self.assertEqual(result["wcag"]["aaa_normal"], False)


if __name__ == "__main__":
    unittest.main()
