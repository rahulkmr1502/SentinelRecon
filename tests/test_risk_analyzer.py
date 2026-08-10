import unittest

from core.cve import CVE
from core.risk_analyzer import analyze_risk


class TestRiskAnalyzer(unittest.TestCase):

    def test_critical_risk(self):
        cves = [
            CVE(
                cve_id="CVE-TEST-001",
                description="Critical vulnerability",
                severity="CRITICAL",
                cvss_score=9.8,
                published="2024-01-01",
                last_modified="2024-01-01",
            )
        ]

        result = analyze_risk(cves)

        self.assertEqual(result.critical, 1)
        self.assertEqual(result.high, 0)
        self.assertEqual(result.medium, 0)
        self.assertEqual(result.low, 0)
        self.assertEqual(result.total, 1)
        self.assertEqual(result.average_cvss, 9.8)
        self.assertEqual(result.overall_risk, "Critical")

    def test_mixed_risk(self):
        cves = [
            CVE(
                cve_id="CVE-TEST-001",
                description="Critical vulnerability",
                severity="CRITICAL",
                cvss_score=9.8,
                published="2024-01-01",
                last_modified="2024-01-01",
            ),
            CVE(
                cve_id="CVE-TEST-002",
                description="High vulnerability",
                severity="HIGH",
                cvss_score=8.0,
                published="2024-01-01",
                last_modified="2024-01-01",
            ),
            CVE(
                cve_id="CVE-TEST-003",
                description="Medium vulnerability",
                severity="MEDIUM",
                cvss_score=5.0,
                published="2024-01-01",
                last_modified="2024-01-01",
            ),
            CVE(
                cve_id="CVE-TEST-004",
                description="Low vulnerability",
                severity="LOW",
                cvss_score=2.0,
                published="2024-01-01",
                last_modified="2024-01-01",
            ),
        ]

        result = analyze_risk(cves)

        self.assertEqual(result.critical, 1)
        self.assertEqual(result.high, 1)
        self.assertEqual(result.medium, 1)
        self.assertEqual(result.low, 1)
        self.assertEqual(result.total, 4)
        self.assertEqual(result.average_cvss, 6.2)
        self.assertEqual(result.overall_risk, "Critical")

    def test_empty_cves(self):
        result = analyze_risk([])

        self.assertEqual(result.critical, 0)
        self.assertEqual(result.high, 0)
        self.assertEqual(result.medium, 0)
        self.assertEqual(result.low, 0)
        self.assertEqual(result.informational, 0)
        self.assertEqual(result.total, 0)
        self.assertEqual(result.average_cvss, 0.0)
        self.assertEqual(result.overall_risk, "None")


if __name__ == "__main__":
    unittest.main()