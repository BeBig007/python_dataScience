from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))                  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))                  # output: 0
print(count_in_list([], "toto"))                                        # output: 0
print(count_in_list(["toto", "tata", "tutu"], "tata"))                  # output: 1
print(count_in_list(["toto", "tata", "toto", "tata", "toto"], "toto"))  # output: 3
print(count_in_list([1, 2, 3, 1], 1))                                   # output: 2
print(count_in_list(["abc", "def", "ghi"], "xyz"))                      # output: 0
print(count_in_list(["", "abc", "", "def", "", "ghi"], ""))             # output: 3
print(count_in_list(["", "", "", "", ""], ""))                          # output: 5

