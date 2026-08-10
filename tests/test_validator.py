import unittest

from core.validator import (
    is_valid_domain,
    is_valid_ip,
    validate_target,
)


class TestValidator(unittest.TestCase):

    # ----------------------------------------------------------
    # IP Validation
    # ----------------------------------------------------------

    def test_valid_ipv4(self):

        self.assertTrue(
            is_valid_ip("192.168.1.1")
        )

    def test_valid_ipv6(self):

        self.assertTrue(
            is_valid_ip("2001:db8::1")
        )

    def test_invalid_ip(self):

        self.assertFalse(
            is_valid_ip("999.999.999.999")
        )

    # ----------------------------------------------------------
    # Domain Validation
    # ----------------------------------------------------------

    def test_valid_domain(self):

        self.assertTrue(
            is_valid_domain("example.com")
        )

        self.assertTrue(
            is_valid_domain("sub.example.com")
        )

    def test_invalid_domain(self):

        self.assertFalse(
            is_valid_domain("example")
        )

        self.assertFalse(
            is_valid_domain("-example.com")
        )

        self.assertFalse(
            is_valid_domain("example-.com")
        )

    # ----------------------------------------------------------
    # Combined Validation
    # ----------------------------------------------------------

    def test_validate_target_with_ip(self):

        self.assertTrue(
            validate_target("192.168.1.1")
        )

    def test_validate_target_with_domain(self):

        self.assertTrue(
            validate_target("example.com")
        )

    def test_validate_invalid_target(self):

        self.assertFalse(
            validate_target("not-a-valid-target")
        )


if __name__ == "__main__":
    unittest.main()