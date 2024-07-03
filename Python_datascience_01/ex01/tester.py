from array2D import slice_me


def main():
    color_reset = "\033[0m"
    color_shape = "\033[94m"  # Blue
    color_error = "\033[91m"  # Red

    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

    print(f"{color_shape}------------Slice 1 to 3------------{color_reset}")
    print(slice_me(family, 0, 2))

    print(f"{color_shape}\n------------Slice 2 to 3------------{color_reset}")
    print(slice_me(family, 1, -2))

    print(f"{color_shape}\n------------Slice 0 to 4------------{color_reset}")
    print(slice_me(family, 0, len(family)))

    print(f"{color_shape}\n------------Slice 2 to 2------------{color_reset}")
    print(slice_me(family, 2, 2))

    print(f"{color_shape}\n------------Slice 3 to 1------------{color_reset}")
    print(slice_me(family, 3, 1))

    print(f"{color_error}\n------------Invalid input------------{color_reset}")
    try:
        slice_me([1, 2, 3], 0, 2)
    except ValueError as e:
        print(e)

    print(f"{color_error}\n------------Invalid input------------{color_reset}")
    try:
        slice_me([[1.8, 78.4], [2.15, 102.7, 50.0]], 0, 2)
    except ValueError as e:
        print(e)

    print(f"{color_error}\n------------Invalid input------------{color_reset}")
    try:
        slice_me(
            [[1.8, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]], 0, 2.5
        )
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
