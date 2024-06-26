from load_csv import load


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue
    c_error = "\033[91m"  # Red

    print(f"{c_shape}---------------Load life_expectancy_years---------------{c_reset}")
    print(load("../life_expectancy_years.csv"))

    print(f"{c_error}\n---------------Invalid input---------------{c_reset}")
    try:
        load(1)
    except ValueError as e:
        print(e)

    print(f"{c_error}\n---------------Invalid input---------------{c_reset}")
    try:
        load("life_expectancy_years.csv")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
