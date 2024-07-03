from new_student import Student


def main():
    c_reset = "\033[0m"
    c_shape = "\033[94m"  # Blue
    c_error = "\033[91m"  # Red

    print(f"{c_shape}---------------Basic Test---------------{c_reset}")
    student = Student(name="Edward", surname="agle")
    print(student)

    print(f"{c_error}---------------Error Test---------------{c_reset}")
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)


if __name__ == "__main__":
    main()
