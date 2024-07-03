from give_bmi import give_bmi, apply_limit


def main():
    color_reset = "\033[0m"
    color_shape = "\033[94m"  # Blue
    color_error = "\033[91m"  # Red

    # Test 1: Normal case
    print(f"{color_shape}------------Test 1------------{color_reset}")
    height = [2.71, 1.15]    # in m
    weight = [165.3, 38.4]   # in kg

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    print()

    # Test 2: Extreme values
    print(f"{color_shape}------------Test 2------------{color_reset}")
    height = [1.0, 2.5, 1.8, 1.2]
    weight = [50.0, 200.0, 80.0, 30.0]

    bmi = give_bmi(height, weight)
    print("BMI:", bmi)
    print("BMI type:", type(bmi))
    print("Limit exceeded:", apply_limit(bmi, 25))
    print()

    # Test 3: Non-numeric values
    print(f"{color_error}------------Test 3------------{color_reset}")
    height = [1.75, '1.8', 1.65]
    weight = [70, 80, 60]

    try:
        bmi = give_bmi(height, weight)
    except AssertionError as e:
        print(f"AssertionError: {e}")

    print("Limit exceeded:", apply_limit([], 25))
    print()

    # Test 4: High limit
    print(f"{color_shape}------------Test 4------------{color_reset}")
    height = [1.75, 1.8, 1.65]
    weight = [70, 80, 60]

    bmi = give_bmi(height, weight)
    print("BMI:", bmi)
    print("Limit exceeded (very high limit):", apply_limit(bmi, 1000))
    print()

    # Test 5: Single value list
    print(f"{color_shape}------------Test 5------------{color_reset}")
    height = [1.75]
    weight = [70]

    bmi = give_bmi(height, weight)
    print("BMI:", bmi)
    print("Limit exceeded:", apply_limit(bmi, 25))
    print()

    # Test 6: Different size lists
    print(f"{color_error}------------Test 6------------{color_reset}")
    height = [1.75, 1.8, 1.65]
    weight = [70, 80]

    try:
        bmi = give_bmi(height, weight)
    except AssertionError as e:
        print(f"AssertionError: {e}")

    print("Limit exceeded:", apply_limit([], 25))
    print()


if __name__ == "__main__":
    main()
