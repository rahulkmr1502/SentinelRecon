from core.severity import Severity


def main() -> None:
    print("Available Severity Levels:\n")

    for level in Severity:
        print(level.name, "->", level.value)

    print("\nExample Usage:")
    print(Severity.HIGH)
    print(Severity.HIGH.value)


if __name__ == "__main__":
    main()