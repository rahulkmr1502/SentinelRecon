import unittest

from core.config import ScannerConfig
from core.config_factory import create_scanner_config


class TestConfig(unittest.TestCase):

    def test_default_scanner_config(self):
        config = ScannerConfig()

        self.assertEqual(config.start_port, 1)
        self.assertEqual(config.end_port, 1024)
        self.assertEqual(config.timeout, 1.0)
        self.assertEqual(config.max_workers, 50)

    def test_create_scanner_config(self):
        config_data = {
            "scanner": {
                "start_port": 80,
                "end_port": 443,
                "timeout": 2.0,
                "max_workers": 20,
            }
        }

        config = create_scanner_config(config_data)

        self.assertEqual(config.start_port, 80)
        self.assertEqual(config.end_port, 443)
        self.assertEqual(config.timeout, 2.0)
        self.assertEqual(config.max_workers, 20)

    def test_create_scanner_config_defaults(self):
        config_data = {
            "scanner": {}
        }

        config = create_scanner_config(config_data)

        self.assertEqual(config.start_port, 1)
        self.assertEqual(config.end_port, 1024)
        self.assertEqual(config.timeout, 1.0)
        self.assertEqual(config.max_workers, 50)


if __name__ == "__main__":
    unittest.main()