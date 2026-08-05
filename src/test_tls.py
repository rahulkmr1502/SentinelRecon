from core.tls_analyzer import analyze_tls


def main() -> None:

    result = analyze_tls("google.com")

    print("\nTLS Analysis")
    print("-" * 50)

    print(f"TLS Version        : {result['tls_version']}")
    print(f"Issuer             : {result['issuer']}")
    print(f"Subject            : {result['subject']}")
    print(f"Valid From         : {result['valid_from']}")
    print(f"Valid Until        : {result['valid_until']}")
    print(f"Certificate Status : {result['certificate_status']}")
    print(f"Days Remaining     : {result['days_remaining']}")


if __name__ == "__main__":
    main()