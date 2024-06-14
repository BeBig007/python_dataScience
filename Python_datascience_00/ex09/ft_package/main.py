from ft_package import count_in_list


def main():
    print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0


if __name__ == "__main__":
    main()

# pip show -v ft_package
# Name: ft_package
# Version: 0.0.1
# Summary: A sample test package
# Home-page: https://github.com/eagle/ft_package
# Author: eagle
# Author-email: eagle@42.fr
# License: MIT
# Location: /home/eagle/...
# Requires:
# Required-by:
# Metadata-Version: 2.1
# Installer: pip
# Classifiers:
# Entry-points: