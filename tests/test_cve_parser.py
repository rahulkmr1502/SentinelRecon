import unittest

from core.cve_parser import parse_cves


class TestCVEParser(unittest.TestCase):

    def test_parse_cve(self):
        data = {
            "vulnerabilities": [
                {
                    "cve": {
                        "id": "CVE-2024-12345",
                        "descriptions": [
                            {
                                "lang": "en",
                                "value": "Example vulnerability.",
                            }
                        ],
                        "metrics": {
                            "cvssMetricV31": [
                                {
                                    "cvssData": {
                                        "baseSeverity": "HIGH",
                                        "baseScore": 8.8,
                                    }
                                }
                            ]
                        },
                        "published": "2024-01-15",
                        "lastModified": "2024-02-01",
                    }
                }
            ]
        }

        cves = parse_cves(data)

        self.assertEqual(len(cves), 1)

        cve = cves[0]

        self.assertEqual(cve.cve_id, "CVE-2024-12345")
        self.assertEqual(cve.description, "Example vulnerability.")
        self.assertEqual(cve.severity, "HIGH")
        self.assertEqual(cve.cvss_score, 8.8)
        self.assertEqual(cve.published, "2024-01-15")
        self.assertEqual(cve.last_modified, "2024-02-01")

    def test_empty_response(self):
        data = {
            "vulnerabilities": []
        }

        cves = parse_cves(data)

        self.assertEqual(cves, [])

    def test_missing_vulnerabilities_key(self):
        data = {}

        cves = parse_cves(data)

        self.assertEqual(cves, [])


if __name__ == "__main__":
    unittest.main()