from load_image import ft_load


def main():
    color_reset = "\033[0m"
    color_shape = "\033[94m"  # Blue
    color_error = "\033[91m"  # Red
    print(f"{color_shape}---------------Load landscape---------------{color_reset}")
    print(ft_load("landscape.jpg"))
    print(f"{color_shape}\n---------------Load animal---------------{color_reset}")
    print(ft_load("animal.jpeg"))
    print(f"{color_error}\n---------------Invalid input---------------{color_reset}")
    try:
        ft_load(1)
    except ValueError as e:
        print(e)
    print(f"{color_error}\n---------------Invalid input---------------{color_reset}")
    try:
        ft_load("land.png")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

# pip install pillow
# $> python3 tester.py
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
# $>