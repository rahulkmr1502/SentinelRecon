import unittest
from unittest.mock import MagicMock, patch

from core.config import ScannerConfig
from core.port_scanner import scan_port, scan_ports


class TestPortScanner(unittest.TestCase):

    @patch("core.port_scanner.socket.socket")
    def test_scan_port_open(self, mock_socket):

        mock_scanner = MagicMock()

        mock_socket.return_value.__enter__.return_value = mock_scanner

        mock_scanner.connect_ex.return_value = 0

        result = scan_port(
            "127.0.0.1",
            80,
            1.0,
        )

        self.assertEqual(result, 80)

        mock_scanner.settimeout.assert_called_once_with(1.0)

        mock_scanner.connect_ex.assert_called_once_with(
            ("127.0.0.1", 80)
        )

    @patch("core.port_scanner.socket.socket")
    def test_scan_port_closed(self, mock_socket):

        mock_scanner = MagicMock()

        mock_socket.return_value.__enter__.return_value = mock_scanner

        mock_scanner.connect_ex.return_value = 111

        result = scan_port(
            "127.0.0.1",
            80,
            1.0,
        )

        self.assertIsNone(result)

    @patch("core.port_scanner.socket.socket")
    def test_scan_port_error(self, mock_socket):

        mock_socket.side_effect = Exception(
            "Socket error"
        )

        result = scan_port(
            "127.0.0.1",
            80,
            1.0,
        )

        self.assertIsNone(result)

    @patch("core.port_scanner.scan_port")
    def test_scan_ports(self, mock_scan_port):

        def fake_scan_port(host, port, timeout):

            if port in [80, 443]:
                return port

            return None

        mock_scan_port.side_effect = fake_scan_port

        config = ScannerConfig(
            start_port=80,
            end_port=443,
            timeout=1.0,
            max_workers=5,
        )

        result = scan_ports(
            "127.0.0.1",
            config,
        )

        self.assertEqual(
            result,
            [80, 443],
        )

        self.assertEqual(
            mock_scan_port.call_count,
            364,
        )


if __name__ == "__main__":
    unittest.main()