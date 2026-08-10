import unittest
from unittest.mock import MagicMock, patch

from core.banner_grabber import grab_banner


class TestBannerGrabber(unittest.TestCase):

    @patch("core.banner_grabber.fingerprint_service")
    @patch("core.banner_grabber.socket.socket")
    def test_http_banner(
        self,
        mock_socket,
        mock_fingerprint,
    ):

        mock_client = MagicMock()

        mock_socket.return_value.__enter__.return_value = mock_client

        mock_client.recv.side_effect = [
            (
                b"HTTP/1.1 200 OK\r\n"
                b"Server: Apache/2.4.7\r\n"
                b"Content-Type: text/html\r\n"
                b"\r\n"
                b"<html>Hello</html>"
            ),
            b"",
        ]

        mock_fingerprint.return_value = {
            "port": 80,
            "service": "HTTP",
            "product": "Apache",
            "version": "2.4.7",
            "banner": (
                "HTTP/1.1 200 OK\r\n"
                "Server: Apache/2.4.7\r\n"
                "Content-Type: text/html"
            ),
        }

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

        self.assertEqual(
            result["version"],
            "2.4.7",
        )

        mock_client.connect.assert_called_once_with(
            ("example.com", 80)
        )

        mock_client.sendall.assert_called_once()

        mock_fingerprint.assert_called_once()


    @patch("core.banner_grabber.fingerprint_service")
    @patch("core.banner_grabber.socket.socket")
    def test_non_http_banner(
        self,
        mock_socket,
        mock_fingerprint,
    ):

        mock_client = MagicMock()

        mock_socket.return_value.__enter__.return_value = mock_client

        mock_client.recv.side_effect = [
            b"SSH-2.0-OpenSSH_8.9\r\n",
            b"",
        ]

        mock_fingerprint.return_value = {
            "port": 22,
            "service": "SSH",
            "product": "OpenSSH",
            "version": "8.9",
            "banner": "SSH-2.0-OpenSSH_8.9",
        }

        result = grab_banner(
            "example.com",
            22,
        )

        self.assertEqual(
            result["port"],
            22,
        )

        self.assertEqual(
            result["service"],
            "SSH",
        )

        self.assertEqual(
            result["product"],
            "OpenSSH",
        )

        self.assertEqual(
            result["version"],
            "8.9",
        )

        mock_client.connect.assert_called_once_with(
            ("example.com", 22)
        )

        # Non-HTTP services should not receive an HTTP request.
        mock_client.sendall.assert_not_called()

        mock_fingerprint.assert_called_once()


    @patch("core.banner_grabber.socket.socket")
    def test_banner_grab_connection_error(
        self,
        mock_socket,
    ):

        mock_socket.side_effect = Exception(
            "Connection failed"
        )

        result = grab_banner(
            "example.com",
            80,
        )

        self.assertEqual(
            result,
            {
                "port": 80,
                "service": "Unknown",
                "product": "Unknown",
                "version": "Unknown",
                "banner": "Unknown",
            },
        )


if __name__ == "__main__":
    unittest.main()