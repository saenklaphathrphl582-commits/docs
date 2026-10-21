from pathlib import Path


def build_message() -> str:
    return "Hello from src/app.py"


def main() -> None:
    print(build_message())


if __name__ == "__main__":
    main()
