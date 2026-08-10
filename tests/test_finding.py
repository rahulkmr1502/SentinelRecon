import unittest

from core.findings import Finding


class TestFinding(unittest.TestCase):

    def test_finding_creation(self):
        finding = Finding(
            title="Missing CSP",
            severity="Medium",
            category="Security Misconfiguration",
            description="Content Security Policy header is missing.",
            recommendation="Configure the Content-Security-Policy header.",
        )

        self.assertEqual(finding.title, "Missing CSP")
        self.assertEqual(finding.severity, "Medium")
        self.assertEqual(
            finding.category,
            "Security Misconfiguration",
        )
        self.assertEqual(
            finding.description,
            "Content Security Policy header is missing.",
        )
        self.assertEqual(
            finding.recommendation,
            "Configure the Content-Security-Policy header.",
        )


if __name__ == "__main__":
    unittest.main()