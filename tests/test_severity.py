import unittest

from core.severity import Severity


class TestSeverity(unittest.TestCase):

    def test_critical(self):
        self.assertEqual(Severity.CRITICAL.value, "Critical")

    def test_high(self):
        self.assertEqual(Severity.HIGH.value, "High")

    def test_medium(self):
        self.assertEqual(Severity.MEDIUM.value, "Medium")

    def test_low(self):
        self.assertEqual(Severity.LOW.value, "Low")

    def test_informational(self):
        self.assertEqual(Severity.INFORMATIONAL.value, "Informational")


if __name__ == "__main__":
    unittest.main()