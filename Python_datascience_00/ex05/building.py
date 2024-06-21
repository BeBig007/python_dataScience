"""This is the module docstring."""
import sys


def ispunctuation(c: str) -> bool:
    """This function checks if the character is a punctuation mark.
    Args:
        c (str): The character to check.
    Returns:
        bool: True if the character is a punctuation mark, False otherwise.
    """
    value = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    return c in value


def main():
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"

        if len(sys.argv) == 1:
            str = input("What is the text to count?\n") + ' '
        else:
            str = sys.argv[1]

        print(f"The text contains {len(str)} characters:")
        print(f"{sum(1 for c in str if c.isupper())} upper letters")
        print(f"{sum(1 for c in str if c.islower())} lower letters")
        print(f"{sum(1 for c in str if ispunctuation(c))} punctuation marks")
        print(f"{sum(1 for c in str if c.isspace())} spaces")
        print(f"{sum(1 for c in str if c.isdigit())} digits")

    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
