import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        arg1 = sys.argv[1]
        assert arg1.replace(" ", "").isalnum(), "the arguments are bad"

        words = arg1.upper()
        word_in_morse = ""
        for c in words:
            if NESTED_MORSE.get(c) is not None:
                word_in_morse += NESTED_MORSE.get(c)
        print(f"{word_in_morse.strip()}")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()

# $> python sos.py "sos" | cat -e
# ... --- ...$
# $> python sos.py 'h$llo'
# AssertionError: the arguments are bad
# $>
