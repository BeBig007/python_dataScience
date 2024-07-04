from DiamondTrap import King


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"    # Blue

    print(f"{c_shape}---------------Joffrey---------------{c_reset}")
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    print("---")

    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print("---")

    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
