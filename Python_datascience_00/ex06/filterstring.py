import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        assert arg1.replace(" ", "").isalpha(), "the arguments are bad"
        assert arg2.isdigit(), "the arguments are bad"

        nb = int(sys.argv[2])
        words = arg1.split()
        filtered_words = list(ft_filter(lambda x: len(x) > nb, words))
        print(filtered_words)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()

    # print(filter.__doc__)
    # print(ft_filter.__doc__)

# $> python filterstring.py 'Hello the World' 4
# ['Hello', 'World']
# $>
# $> python filterstring.py 'Hello the World' 99
# []
# $>
# $> python filterstring.py 3 'Hello the World'
# AssertionError: the arguments are bad
# $>
# $> python filterstring.py
# AssertionError: the arguments are bad
