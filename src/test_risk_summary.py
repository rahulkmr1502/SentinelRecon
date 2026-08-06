from core.risk_summary import RiskSummary


def main() -> None:

    summary = RiskSummary(
        critical=2,
        high=5,
        medium=4,
        low=1,
        total=12,
        average_cvss=8.1,
        overall_risk="High",
    )

    print(summary)


if __name__ == "__main__":
    main()