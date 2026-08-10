import unittest

from core.cve import CVE


class TestCVE(unittest.TestCase):

    def test_cve_creation(self):
        cve = CVE(
            cve_id="CVE-2024-12345",
            description="Example vulnerability.",
            severity="HIGH",
            cvss_score=8.8,
            published="2024-01-15",
            last_modified="2024-02-01",
        )

        self.assertEqual(cve.cve_id, "CVE-2024-12345")
        self.assertEqual(cve.description, "Example vulnerability.")
        self.assertEqual(cve.severity, "HIGH")
        self.assertEqual(cve.cvss_score, 8.8)
        self.assertEqual(cve.published, "2024-01-15")
        self.assertEqual(cve.last_modified, "2024-02-01")


if __name__ == "__main__":
    unittest.main()