import unittest

from core.cve import CVE
from core.findings import Finding
from core.report_generator import generate_html_report
from core.risk_summary import RiskSummary


class TestReportGenerator(unittest.TestCase):

    def test_generate_html_report(self):

        services = [
            {
                "port": 80,
                "service": "HTTP",
                "product": "Apache",
                "version": "2.4.7",
            }
        ]

        findings = [
            Finding(
                title="Missing CSP",
                severity="Medium",
                category="Security Misconfiguration",
                description="Content Security Policy header is missing.",
                recommendation="Configure the Content-Security-Policy header.",
            )
        ]

        cves = [
            CVE(
                cve_id="CVE-2024-12345",
                description="Example vulnerability.",
                severity="HIGH",
                cvss_score=8.8,
                published="2024-01-15",
                last_modified="2024-02-01",
            )
        ]

        summary = RiskSummary(
            critical=0,
            high=1,
            medium=1,
            low=0,
            informational=0,
            total=1,
            average_cvss=8.8,
            overall_risk="High",
        )

        report_path = generate_html_report(
            target="test-target",
            services=services,
            findings=findings,
            cves=cves,
            summary=summary,
        )

        self.assertTrue(report_path.exists())

        html = report_path.read_text(encoding="utf-8")

        # Target
        self.assertIn("test-target", html)

        # Service
        self.assertIn("Apache", html)
        self.assertIn("2.4.7", html)

        # Finding
        self.assertIn("Missing CSP", html)
        self.assertIn("Security Misconfiguration", html)

        # CVE
        self.assertIn("CVE-2024-12345", html)
        self.assertIn("8.8", html)

        # Risk summary
        self.assertIn("High", html)
        self.assertIn("Average CVSS", html)

        # Cleanup
        report_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()