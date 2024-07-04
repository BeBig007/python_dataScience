from S1E7 import Baratheon, Lannister


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"    # Blue
    c_dict = "\033[93m"     # Yellow
    c_str = "\033[92m"      # Green
    c_repr = "\033[91m"     # Red
    c_alive = "\033[95m"    # Purple
    c_doc = "\033[96m"      # Cyan

    print(f"{c_shape}---------------Robert---------------{c_reset}")
    Robert = Baratheon("Robert")
    print(f"{c_dict}{Robert.__dict__}{c_reset}")
    print("---")

    print(f"{c_str}{Robert.__str__}{c_reset}")
    print(f"{c_repr}{Robert.__repr__}{c_reset}")
    print("---")

    print(f"{c_alive}{Robert.is_alive}{c_reset}")
    Robert.die()
    print(f"{c_alive}{Robert.is_alive}{c_reset}")
    print("---")

    print(f"{c_doc}{Robert.__doc__}{c_reset}")

    print(f"{c_shape}---------------Cersei---------------{c_reset}")
    Cersei = Lannister("Cersei")
    print(f"{c_dict}{Cersei.__dict__}{c_reset}")
    print(f"{c_str}{Cersei.__str__}{c_reset}")
    print("---")

    print(f"{c_alive}{Cersei.is_alive}{c_reset}")

    print(f"{c_shape}---------------Jaine---------------{c_reset}")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, "
          f"Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
