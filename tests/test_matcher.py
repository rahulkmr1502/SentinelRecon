import unittest
from unittest.mock import patch

from core.cve import CVE
from core.cve_matcher import lookup_service_cves


class TestCVEMatcher(unittest.TestCase):

    @patch("core.cve_matcher.search_cves")
    def test_lookup_service_cves(self, mock_search):

        mock_search.return_value = {
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

        result = lookup_service_cves(
            "Apache",
            "2.4.7",
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].cve_id, "CVE-2024-12345")
        self.assertEqual(result[0].severity, "HIGH")
        self.assertEqual(result[0].cvss_score, 8.8)

        mock_search.assert_called_once()


if __name__ == "__main__":
    unittest.main()