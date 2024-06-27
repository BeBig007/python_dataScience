from load_csv import load
from projection_life import projection_life


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue

    print(f"{c_shape}---------------Load file--------------{c_reset}")
    inc = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load('../life_expectancy_years.csv')
    projection_life(inc, life_expectancy)


if __name__ == "__main__":
    main()
