import socket
import unittest
from unittest.mock import patch

from core.dns_resolver import resolve_target


class TestDNSResolver(unittest.TestCase):

    @patch("core.dns_resolver.socket.getaddrinfo")
    def test_resolve_target_success(self, mock_getaddrinfo):

        mock_getaddrinfo.return_value = [
            (
                socket.AF_INET,
                socket.SOCK_STREAM,
                6,
                "",
                ("192.168.1.10", 0),
            ),
            (
                socket.AF_INET,
                socket.SOCK_STREAM,
                6,
                "",
                ("192.168.1.10", 0),
            ),
            (
                socket.AF_INET,
                socket.SOCK_STREAM,
                6,
                "",
                ("192.168.1.20", 0),
            ),
        ]

        result = resolve_target("example.com")

        self.assertEqual(
            result,
            [
                "192.168.1.10",
                "192.168.1.20",
            ],
        )

        mock_getaddrinfo.assert_called_once_with(
            "example.com",
            None,
            family=socket.AF_UNSPEC,
            type=socket.SOCK_STREAM,
        )

    @patch("core.dns_resolver.socket.getaddrinfo")
    def test_resolve_target_failure(self, mock_getaddrinfo):

        mock_getaddrinfo.side_effect = socket.gaierror(
            "DNS resolution failed"
        )

        result = resolve_target("invalid.example")

        self.assertEqual(result, [])

        mock_getaddrinfo.assert_called_once_with(
            "invalid.example",
            None,
            family=socket.AF_UNSPEC,
            type=socket.SOCK_STREAM,
        )


if __name__ == "__main__":
    unittest.main()