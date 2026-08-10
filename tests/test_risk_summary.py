import unittest

from core.risk_summary import RiskSummary


class TestRiskSummary(unittest.TestCase):

    def test_risk_summary_creation(self):
        summary = RiskSummary(
            critical=1,
            high=1,
            medium=1,
            low=1,
            informational=0,
            total=4,
            average_cvss=6.83,
            overall_risk="Critical",
        )

        self.assertEqual(summary.critical, 1)
        self.assertEqual(summary.high, 1)
        self.assertEqual(summary.medium, 1)
        self.assertEqual(summary.low, 1)
        self.assertEqual(summary.informational, 0)
        self.assertEqual(summary.total, 4)
        self.assertEqual(summary.average_cvss, 6.83)
        self.assertEqual(summary.overall_risk, "Critical")


if __name__ == "__main__":
    unittest.main()