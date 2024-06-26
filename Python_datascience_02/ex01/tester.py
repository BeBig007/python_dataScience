from load_csv import load
from aff_life import aff_life


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue

    print(f"{c_shape}---------------Load life_expectancy_years---------------{c_reset}")
    data = load("../life_expectancy_years.csv")
    aff_life(data)


if __name__ == "__main__":
    main()
