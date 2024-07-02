from in_out import outer
from in_out import square
from in_out import pow


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue
    c_light = "\033[95m"  # Purple
    c_error = "\033[91m"  # Red

    print(f"{c_shape}---------------Basic Test---------------{c_reset}")
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print(f"{c_light}-----{c_reset}")

    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())

    print(f"{c_error}---------------Error Test---------------{c_reset}")
    try:
        another_another_counter = outer(1.5, abs)
        print(another_another_counter())
        print(another_another_counter())
        print(another_another_counter())
    except ValueError as msg:
        print(msg)
    print(f"{c_light}-----{c_reset}")

    try:
        another_another_another_counter = outer('a', pow)
        print(another_another_another_counter())
        print(another_another_another_counter())
        print(another_another_another_counter())
    except ValueError as msg:
        print(msg)


if __name__ == '__main__':
    main()
