from core.config_factory import create_scanner_config
from core.config_loader import load_config


def main():

    config = load_config()

    scanner_config = create_scanner_config(config)

    print("\nScanner Configuration")
    print("=" * 40)

    print(f"Start Port  : {scanner_config.start_port}")
    print(f"End Port    : {scanner_config.end_port}")
    print(f"Timeout     : {scanner_config.timeout}")
    print(f"Max Workers : {scanner_config.max_workers}")


if __name__ == "__main__":
    main()