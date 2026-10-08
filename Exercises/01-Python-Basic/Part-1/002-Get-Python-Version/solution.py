import sys


def get_python_version() -> None:
    """Prints the current Python version and detailed version info."""
    print("Pyhon Version: ")
    print(sys.version)
    print("Version Info: ")
    print(sys.version_info)


def main() -> None:
    get_python_version()


if __name__ == "__main__":
    main()
