import unittest
from unittest.mock import Mock, patch

from core.nvd_client import search_cves


class TestNVDClient(unittest.TestCase):

    @patch("core.nvd_client.requests.get")
    def test_search_cves_success(self, mock_get):

        mock_response = Mock()

        mock_response.json.return_value = {
            "resultsPerPage": 1,
            "vulnerabilities": [
                {
                    "cve": {
                        "id": "CVE-2024-12345"
                    }
                }
            ]
        }

        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = search_cves("Apache")

        self.assertIn("vulnerabilities", result)
        self.assertEqual(
            result["vulnerabilities"][0]["cve"]["id"],
            "CVE-2024-12345",
        )

        mock_get.assert_called_once_with(
            "https://services.nvd.nist.gov/rest/json/cves/2.0",
            params={
                "keywordSearch": "Apache",
                "resultsPerPage": 5,
            },
            timeout=15,
        )

    @patch("core.nvd_client.requests.get")
    def test_search_cves_request_error(self, mock_get):

        import requests

        mock_get.side_effect = requests.RequestException(
            "Connection failed"
        )

        result = search_cves("Apache")

        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()