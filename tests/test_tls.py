import unittest
from unittest.mock import MagicMock, patch

from core.tls_analyzer import analyze_tls


class TestTLSAnalyzer(unittest.TestCase):

    @patch("core.tls_analyzer.ssl.create_default_context")
    @patch("core.tls_analyzer.socket.create_connection")
    def test_analyze_tls_success(
        self,
        mock_create_connection,
        mock_create_context,
    ):

        mock_socket = MagicMock()
        mock_tls_socket = MagicMock()

        mock_create_connection.return_value.__enter__.return_value = (
            mock_socket
        )

        mock_context = MagicMock()
        mock_create_context.return_value = mock_context

        mock_context.wrap_socket.return_value.__enter__.return_value = (
            mock_tls_socket
        )

        mock_tls_socket.getpeercert.return_value = {
            "issuer": [
                [
                    ("organizationName", "Test Certificate Authority"),
                ]
            ],
            "subject": [
                [
                    ("commonName", "example.com"),
                ]
            ],
            "notBefore": "Jan 01 00:00:00 2026 GMT",
            "notAfter": "Dec 31 23:59:59 2026 GMT",
        }

        mock_tls_socket.version.return_value = "TLSv1.3"

        result = analyze_tls("example.com")

        self.assertEqual(
            result["tls_version"],
            "TLSv1.3",
        )

        self.assertEqual(
            result["issuer"],
            "Test Certificate Authority",
        )

        self.assertEqual(
            result["subject"],
            "example.com",
        )

        self.assertEqual(
            result["valid_from"],
            "Jan 01 00:00:00 2026 GMT",
        )

        self.assertEqual(
            result["valid_until"],
            "Dec 31 23:59:59 2026 GMT",
        )

        self.assertEqual(
            result["certificate_status"],
            "Valid",
        )

        self.assertIsInstance(
            result["days_remaining"],
            int,
        )

        mock_create_connection.assert_called_once_with(
            ("example.com", 443),
            timeout=5,
        )

        mock_context.wrap_socket.assert_called_once_with(
            mock_socket,
            server_hostname="example.com",
        )

    @patch("core.tls_analyzer.ssl.create_default_context")
    @patch("core.tls_analyzer.socket.create_connection")
    def test_analyze_tls_connection_error(
        self,
        mock_create_connection,
        mock_create_context,
    ):

        mock_create_connection.side_effect = Exception(
            "Connection failed"
        )

        result = analyze_tls("example.com")

        self.assertEqual(
            result["tls_version"],
            "Unknown",
        )

        self.assertEqual(
            result["issuer"],
            "Unknown",
        )

        self.assertEqual(
            result["subject"],
            "Unknown",
        )

        self.assertEqual(
            result["certificate_status"],
            "Unknown",
        )

        self.assertEqual(
            result["days_remaining"],
            "Unknown",
        )


if __name__ == "__main__":
    unittest.main()