import json
import unittest
from pathlib import Path
from unittest.mock import patch

from core.cve import CVE
from core.findings import Finding
from core.json_report_generator import generate_json_report
from core.risk_summary import RiskSummary


class TestJSONReport(unittest.TestCase):

    @patch("core.json_report_generator.datetime")
    def test_generate_json_report(self, mock_datetime):

        mock_datetime.now.return_value.isoformat.return_value = (
            "2026-08-10T12:00:00"
        )

        mock_datetime.now.return_value.strftime.return_value = (
            "20260810_120000"
        )

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
                description="CSP header is missing.",
                recommendation="Configure CSP.",
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

        report_path = generate_json_report(
            target="test-target",
            services=services,
            findings=findings,
            cves=cves,
            summary=summary,
        )

        self.assertTrue(report_path.exists())

        data = json.loads(report_path.read_text(encoding="utf-8"))

        self.assertEqual(data["target"], "test-target")

        self.assertEqual(
            data["generated_at"],
            "2026-08-10T12:00:00",
        )

        self.assertEqual(len(data["services"]), 1)
        self.assertEqual(data["services"][0]["port"], 80)

        self.assertEqual(len(data["security_findings"]), 1)
        self.assertEqual(
            data["security_findings"][0]["title"],
            "Missing CSP",
        )

        self.assertEqual(len(data["known_vulnerabilities"]), 1)
        self.assertEqual(
            data["known_vulnerabilities"][0]["cve_id"],
            "CVE-2024-12345",
        )

        self.assertEqual(
            data["risk_summary"]["overall_risk"],
            "High",
        )

        self.assertEqual(
            data["risk_summary"]["average_cvss"],
            8.8,
        )

        # Cleanup generated test report
        report_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()