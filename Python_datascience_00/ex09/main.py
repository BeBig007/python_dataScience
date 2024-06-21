from ft_package import count_in_list


def main():
    print(count_in_list(["toto", "tata", "toto"], "toto"))                  # 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))                  # 0
    print(count_in_list([], "toto"))                                        # 0
    print(count_in_list(["toto", "tata", "tutu"], "tata"))                  # 1
    print(count_in_list(["toto", "tata", "toto", "tata", "toto"], "toto"))  # 3
    print(count_in_list([1, 2, 3, 1], 1))                                   # 2
    print(count_in_list(["abc", "def", "ghi"], "xyz"))                      # 0
    print(count_in_list(["", "abc", "", "def", "", "ghi"], ""))             # 3
    print(count_in_list(["", "", "", "", ""], ""))                          # 5


if __name__ == "__main__":
    main()
