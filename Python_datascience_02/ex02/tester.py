from load_csv import load
from aff_pop import aff_pop


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue

    print(f"{c_shape}---------------Load file---------------{c_reset}")
    data = load("../population_total.csv")
    aff_pop(data)


if __name__ == "__main__":
    main()
