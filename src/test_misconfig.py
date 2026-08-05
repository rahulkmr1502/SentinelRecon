from core.http_analyzer import analyze_http
from core.misconfig_detector import detect_http_misconfigurations


def main() -> None:
    result = analyze_http("google.com")

    findings = detect_http_misconfigurations(result)

    print("\nDetected Findings")
    print("=" * 70)

    for finding in findings:
        print(f"Title          : {finding.title}")
        print(f"Severity       : {finding.severity}")
        print(f"Category       : {finding.category}")
        print(f"Description    : {finding.description}")
        print(f"Recommendation : {finding.recommendation}")
        print("-" * 70)


if __name__ == "__main__":
    main()