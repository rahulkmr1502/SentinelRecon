from logger import logger
from validator import validate_target


def main() -> None:
    target = input("Enter an IP address or domain: ").strip()

    if validate_target(target):
        logger.info("Accepted target: %s", target)
        print(f"Target '{target}' is valid.")
    else:
        logger.warning("Invalid target: %s", target)
        print("Invalid IP address or domain.")


if __name__ == "__main__":
    main()