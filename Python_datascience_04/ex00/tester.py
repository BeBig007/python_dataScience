from statistics import ft_statistics


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue
    c_light = "\033[95m"  # Purple
    c_error = "\033[91m"  # Red

    print(f"{c_shape}---------------Basic Test---------------{c_reset}")
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print(f"{c_light}-----{c_reset}")

    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print(f"{c_light}-----{c_reset}")

    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print(f"{c_light}-----{c_reset}")

    ft_statistics(toto="mean", tutu="median", tata="quartile")

    print(f"{c_error}---------------Error Test---------------{c_reset}")
    ft_statistics()
    print(f"{c_light}-----{c_reset}")

    ft_statistics(1, toto="mean", tutu="median", tata="quartile",
                  hello="std", world="var")
    print(f"{c_light}-----{c_reset}")

    ft_statistics("a", "b", "c", toto="mean")
    print(f"{c_light}-----{c_reset}")

    ft_statistics(1, 2, 3, toto="max")


if __name__ == "__main__":
    main()
