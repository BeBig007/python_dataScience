import sys


def main():
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
        str = sys.argv[1]
        print(f"The text contains {len(str)} characters:")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
