import socket
import ssl
from datetime import datetime, timezone


def analyze_tls(host: str, port: int = 443) -> dict:
    """
    Retrieve TLS certificate information and analyze its validity.
    """

    context = ssl.create_default_context()

    try:
        with socket.create_connection((host, port), timeout=5) as sock:

            with context.wrap_socket(sock, server_hostname=host) as tls_socket:

                cert = tls_socket.getpeercert()

                issuer = dict(x[0] for x in cert.get("issuer", []))
                subject = dict(x[0] for x in cert.get("subject", []))

                valid_from = cert.get("notBefore", "")
                valid_until = cert.get("notAfter", "")

                expiry_date = datetime.strptime(
                    valid_until,
                    "%b %d %H:%M:%S %Y %Z",
                ).replace(tzinfo=timezone.utc)

                today = datetime.now(timezone.utc)

                days_remaining = (expiry_date - today).days

                certificate_status = (
                    "Valid"
                    if days_remaining >= 0
                    else "Expired"
                )

                tls_version = tls_socket.version()

                return {
                    "tls_version": tls_version,
                    "issuer": issuer.get("organizationName", "Unknown"),
                    "subject": subject.get("commonName", "Unknown"),
                    "valid_from": valid_from,
                    "valid_until": valid_until,
                    "certificate_status": certificate_status,
                    "days_remaining": days_remaining,
                }

    except Exception:
        return {
            "tls_version": "Unknown",
            "issuer": "Unknown",
            "subject": "Unknown",
            "valid_from": "Unknown",
            "valid_until": "Unknown",
            "certificate_status": "Unknown",
            "days_remaining": "Unknown",
        }