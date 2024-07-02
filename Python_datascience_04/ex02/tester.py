from callLimit import callLimit


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue
    c_error = "\033[91m"  # Red

    print(f"{c_shape}---------------Basic Test---------------{c_reset}")

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()

    print(f"{c_error}---------------Error Test---------------{c_reset}")
    try:
        @callLimit('a')
        def f():
            print("f()")
    except AssertionError as e:
        print(e)

    try:
        @callLimit(1)
        def g():
            print("g()")

        for i in range(3):
            f()
            g()

    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
