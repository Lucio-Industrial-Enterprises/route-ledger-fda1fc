import unittest

from warehouse.sku import normalize_sku


class SkuTests(unittest.TestCase):
    def test_canonical_sku(self):
        cases = (
            (" a-12 ", "A-12"),
            ("a-12", "A-12"),
            ("A-12", "A-12"),
            ("\t aB-12 \n", "AB-12"),
        )
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(normalize_sku(value), expected)

    def test_blank_sku(self):
        for value in ("", "  ", "\t\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_sku(value)
