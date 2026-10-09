import datetime


def print_current_datetime() -> None:
    """Fetches and displays the current date and time in a formatted string."""
    now = datetime.datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time : ")
    print(formatted_now)


def main() -> None:
    print_current_datetime()


if __name__ == "__main__":
    main()
