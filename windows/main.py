# main.py


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """Main entry point of the program."""
    print(greet("World"))


if __name__ == "__main__":
    main()
