import sys

try:
    if len(sys.argv) == 1:
        sys.exit()

    assert len(sys.argv) == 2, "more than one argument is provided"

    arg = sys.argv[1]
    assert arg.lstrip('-').isdigit(), "argument is not an integer"
    number = int(arg)

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as msg:
    print(f"AssertionError: {msg}")
