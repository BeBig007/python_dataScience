
def give_bmi(
    height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    """Calculate Body Mass Index (BMI) for each pair of height and weight."""

    try:
        assert isinstance(height, list) and isinstance(weight, list), \
            "height or weight is not a list"

        assert all(isinstance(h, (int, float)) for h in height), \
            "Elements in height list are not int/floats"

        assert all(isinstance(w, (int, float)) for w in weight), \
            "Elements in weight list are not int/floats"

        assert len(height) == len(weight), "lists are not the same size"

        return [weight[i] / (height[i] ** 2) for i in range(len(height))]

    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if each BMI value in the list exceeds the specified limit."""

    try:
        assert isinstance(bmi, list) and isinstance(limit, int), \
            "bmi must be a list & limit an int"

        assert all(isinstance(h, (int, float)) for h in bmi), \
            "Elements in bmi list are not int/floats"

        return [value > limit for value in bmi]

    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    return None
