import json
import unittest
from pathlib import Path
from unittest.mock import patch

from core.banner_grabber import grab_banner
from core.cve_matcher import lookup_service_cves
from core.dns_resolver import resolve_target
from core.json_report_generator import generate_json_report
from core.misconfig_detector import detect_http_misconfigurations
from core.port_scanner import scan_ports
from core.risk_analyzer import analyze_risk
from core.tls_analyzer import analyze_tls
from core.validator import validate_target


class TestSentinelReconIntegration(unittest.TestCase):

    @patch("core.dns_resolver.socket.getaddrinfo")
    @patch("core.port_scanner.scan_port")
    def test_target_to_port_scanning_flow(
        self,
        mock_scan_port,
        mock_getaddrinfo,
    ):
        """Test target validation, DNS resolution, and port scanning."""

        target = "example.com"

        self.assertTrue(validate_target(target))

        mock_getaddrinfo.return_value = [
            (
                2,
                1,
                6,
                "",
                ("93.184.216.34", 0),
            )
        ]

        addresses = resolve_target(target)

        self.assertEqual(
            addresses,
            ["93.184.216.34"],
        )

        def fake_scan_port(host, port, timeout):
            if port in (80, 443):
                return port
            return None

        mock_scan_port.side_effect = fake_scan_port

        from core.config import ScannerConfig

        config = ScannerConfig(
            start_port=80,
            end_port=443,
            timeout=1.0,
            max_workers=2,
        )

        open_ports = scan_ports(
            "93.184.216.34",
            config,
        )

        self.assertEqual(
            open_ports,
            [80, 443],
        )

    @patch("core.banner_grabber.socket.socket")
    def test_port_to_service_fingerprinting_flow(
        self,
        mock_socket,
    ):
        """Test banner grabbing and service fingerprinting."""

        mock_client = (
            mock_socket.return_value.__enter__.return_value
        )

        mock_client.recv.side_effect = [
            (
                b"HTTP/1.1 200 OK\r\n"
                b"Server: Apache/2.4.7\r\n"
                b"Content-Type: text/html\r\n\r\n"
            ),
            b"",
        ]

        result = grab_banner(
            "example.com",
            80,
        )

        self.assertEqual(
            result["port"],
            80,
        )

        self.assertEqual(
            result["service"],
            "HTTP",
        )

        self.assertEqual(
            result["product"],
            "Apache",
        )

    def test_http_to_misconfiguration_flow(self):
        """Test HTTP analysis and security misconfiguration detection."""

        http_result = {
            "status_code": "200",
            "server": "Apache",
            "content_type": "text/html",
            "headers": {
                "Server": "Apache",
                "Content-Type": "text/html",
            },
            "security_headers": {
                "Strict-Transport-Security": False,
                "Content-Security-Policy": False,
                "X-Frame-Options": True,
                "X-Content-Type-Options": True,
                "Referrer-Policy": True,
                "Permissions-Policy": True,
            },
        }

        findings = detect_http_misconfigurations(
            http_result
        )

        self.assertEqual(
            len(findings),
            2,
        )

        titles = [
            finding.title
            for finding in findings
        ]

        self.assertIn(
            "Missing Content-Security-Policy Header",
            titles,
        )

        self.assertIn(
            "Missing Strict-Transport-Security Header",
            titles,
        )

    @patch("core.cve_matcher.search_cves")
    def test_cve_to_risk_analysis_flow(
        self,
        mock_search_cves,
    ):
        """Test CVE lookup, parsing, and risk analysis."""

        mock_search_cves.return_value = {
            "vulnerabilities": [
                {
                    "cve": {
                        "id": "CVE-2021-44228",
                        "descriptions": [
                            {
                                "lang": "en",
                                "value": (
                                    "Example critical vulnerability."
                                ),
                            }
                        ],
                        "published": (
                            "2021-12-10T00:00:00.000"
                        ),
                        "lastModified": (
                            "2021-12-15T00:00:00.000"
                        ),
                        "metrics": {
                            "cvssMetricV31": [
                                {
                                    "cvssData": {
                                        "baseScore": 10.0,
                                        "baseSeverity": "CRITICAL",
                                    }
                                }
                            ]
                        },
                    }
                }
            ]
        }

        cves = lookup_service_cves(
            "Log4j",
            "2.14.1",
        )

        self.assertEqual(
            len(cves),
            1,
        )

        self.assertEqual(
            cves[0].cve_id,
            "CVE-2021-44228",
        )

        risk_summary = analyze_risk(cves)

        self.assertEqual(
            risk_summary.critical,
            1,
        )

        self.assertEqual(
            risk_summary.total,
            1,
        )

        self.assertEqual(
            risk_summary.overall_risk,
            "Critical",
        )

    @patch("core.tls_analyzer.socket.create_connection")
    def test_tls_analysis_flow(
        self,
        mock_connection,
    ):
        """Test TLS certificate analysis."""

        mock_socket_instance = (
            mock_connection.return_value.__enter__.return_value
        )

        with patch(
            "core.tls_analyzer.ssl.create_default_context"
        ) as mock_context:

            context_instance = (
                mock_context.return_value
            )

            context_instance.wrap_socket.return_value.__enter__.return_value = (
                mock_socket_instance
            )

            mock_socket_instance.getpeercert.return_value = {
                "issuer": [
                    [
                        (
                            "organizationName",
                            "Example CA",
                        )
                    ]
                ],
                "subject": [
                    [
                        (
                            "commonName",
                            "example.com",
                        )
                    ]
                ],
                "notBefore": (
                    "Jan 01 00:00:00 2030 GMT"
                ),
                "notAfter": (
                    "Jan 01 00:00:00 2031 GMT"
                ),
            }

            mock_socket_instance.version.return_value = (
                "TLSv1.3"
            )

            result = analyze_tls(
                "example.com"
            )

            self.assertEqual(
                result["tls_version"],
                "TLSv1.3",
            )

            self.assertEqual(
                result["issuer"],
                "Example CA",
            )

            self.assertEqual(
                result["subject"],
                "example.com",
            )

    def test_risk_to_json_report_flow(self):
        """Test risk analysis and JSON report generation."""

        cves = []

        risk_summary = analyze_risk(cves)

        services = [
            {
                "port": 80,
                "service": "HTTP",
                "product": "Apache",
                "version": "2.4.7",
            }
        ]

        findings = []

        report_path = generate_json_report(
            target="integration-test.example",
            services=services,
            findings=findings,
            cves=cves,
            summary=risk_summary,
        )

        self.assertTrue(
            Path(report_path).exists()
        )

        report_data = json.loads(
            Path(report_path).read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(
            report_data["target"],
            "integration-test.example",
        )

        self.assertEqual(
            len(report_data["services"]),
            1,
        )

        self.assertEqual(
            report_data["risk_summary"]["total"],
            0,
        )

        Path(report_path).unlink()


if __name__ == "__main__":
    unittest.main()