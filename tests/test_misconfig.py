import unittest

from core.http_analyzer import analyze_http
from core.misconfig_detector import detect_http_misconfigurations


class TestMisconfigurationDetector(unittest.TestCase):

    def test_missing_security_headers(self):

        http_result = {
            "status_code": 200,
            "server": "Apache",
            "content_type": "text/html",
            "security_headers": {
                "Strict-Transport-Security": False,
                "Content-Security-Policy": False,
                "X-Frame-Options": False,
                "X-Content-Type-Options": False,
                "Referrer-Policy": False,
                "Permissions-Policy": False,
            },
        }

        findings = detect_http_misconfigurations(http_result)

        self.assertGreater(len(findings), 0)

        titles = [finding.title for finding in findings]

        self.assertIn(
            "Missing Strict-Transport-Security Header",
            titles,
        )

        self.assertIn(
            "Missing Content-Security-Policy Header",
            titles,
        )

    def test_no_missing_headers(self):

        http_result = {
            "status_code": 200,
            "server": "Apache",
            "content_type": "text/html",
            "security_headers": {
                "Strict-Transport-Security": True,
                "Content-Security-Policy": True,
                "X-Frame-Options": True,
                "X-Content-Type-Options": True,
                "Referrer-Policy": True,
                "Permissions-Policy": True,
            },
        }

        findings = detect_http_misconfigurations(http_result)

        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()