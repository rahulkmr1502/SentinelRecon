from core.http_analyzer import analyze_http


def main() -> None:
    result = analyze_http("scanme.nmap.org")

    print("\nHTTP Analysis")
    print("-" * 50)

    print(f"Status Code : {result['status_code']}")
    print(f"Server      : {result['server']}")
    print(f"Content-Type: {result['content_type']}")

    print("\nHTTP Headers")
    print("-" * 50)

    for key, value in result["headers"].items():
        print(f"{key}: {value}")

    print("\nSecurity Header Analysis")
    print("-" * 50)

    for header, present in result["security_headers"].items():
        status = "Present" if present else "Missing"
        print(f"{header:<35} {status}")


if __name__ == "__main__":
    main()