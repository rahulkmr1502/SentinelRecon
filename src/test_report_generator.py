from core.report_generator import generate_report_filename


def main():

    filename = generate_report_filename("google.com")

    print(filename)


if __name__ == "__main__":
    main()