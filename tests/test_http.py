import unittest
from unittest.mock import MagicMock, patch

from core.http_analyzer import analyze_http, analyze_security_headers


class TestHTTPAnalyzer(unittest.TestCase):

    @patch("core.http_analyzer.socket.socket")
    def test_analyze_http_success(self, mock_socket):

        mock_client = MagicMock()

        mock_socket.return_value.__enter__.return_value = mock_client

        mock_client.recv.side_effect = [
            (
                b"HTTP/1.1 200 OK\r\n"
                b"Server: Apache\r\n"
                b"Content-Type: text/html\r\n"
                b"Strict-Transport-Security: max-age=31536000\r\n"
                b"Content-Security-Policy: default-src 'self'\r\n"
                b"X-Frame-Options: SAMEORIGIN\r\n"
                b"X-Content-Type-Options: nosniff\r\n"
                b"\r\n"
                b"<html>Hello</html>"
            ),
            b"",
        ]

        result = analyze_http("example.com")

        self.assertEqual(result["status_code"], "200")
        self.assertEqual(result["server"], "Apache")
        self.assertEqual(result["content_type"], "text/html")

        self.assertTrue(
            result["security_headers"]["Strict-Transport-Security"]
        )

        self.assertTrue(
            result["security_headers"]["Content-Security-Policy"]
        )

        self.assertTrue(
            result["security_headers"]["X-Frame-Options"]
        )

        self.assertTrue(
            result["security_headers"]["X-Content-Type-Options"]
        )

        self.assertFalse(
            result["security_headers"]["Referrer-Policy"]
        )

        self.assertFalse(
            result["security_headers"]["Permissions-Policy"]
        )

        mock_client.connect.assert_called_once_with(
            ("example.com", 80)
        )

        mock_client.sendall.assert_called_once()


    @patch("core.http_analyzer.socket.socket")
    def test_analyze_http_connection_error(self, mock_socket):

        mock_socket.side_effect = Exception("Connection failed")

        result = analyze_http("example.com")

        self.assertEqual(result["status_code"], "Unknown")
        self.assertEqual(result["server"], "Unknown")
        self.assertEqual(result["content_type"], "Unknown")
        self.assertEqual(result["headers"], {})
        self.assertEqual(result["security_headers"], {})


    def test_analyze_security_headers(self):

        headers = {
            "Strict-Transport-Security": "max-age=31536000",
            "Content-Security-Policy": "default-src 'self'",
            "X-Frame-Options": "SAMEORIGIN",
            "X-Content-Type-Options": "nosniff",
        }

        result = analyze_security_headers(headers)

        self.assertTrue(
            result["Strict-Transport-Security"]
        )

        self.assertTrue(
            result["Content-Security-Policy"]
        )

        self.assertTrue(
            result["X-Frame-Options"]
        )

        self.assertTrue(
            result["X-Content-Type-Options"]
        )

        self.assertFalse(
            result["Referrer-Policy"]
        )

        self.assertFalse(
            result["Permissions-Policy"]
        )


if __name__ == "__main__":
    unittest.main()