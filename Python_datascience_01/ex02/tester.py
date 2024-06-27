from load_image import ft_load


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue
    c_error = "\033[91m"  # Red

    print(f"{c_shape}---------------Load landscape---------------{c_reset}")
    print(ft_load("landscape.jpg"))

    print(f"{c_shape}\n---------------Load animal---------------{c_reset}")
    print(ft_load("animal.jpeg"))

    print(f"{c_error}\n---------------Invalid input---------------{c_reset}")
    try:
        ft_load(1)
    except ValueError as e:
        print(e)

    print(f"{c_error}\n---------------Invalid input---------------{c_reset}")
    try:
        ft_load("land.png")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
