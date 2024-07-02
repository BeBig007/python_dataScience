
def mean(data: tuple) -> int:
    """Mean"""
    return sum(data) / len(data)


def median(data: tuple) -> int:
    """Median"""
    sorted_data = sorted(data)
    size = len(sorted_data)
    if size % 2 == 0:
        return (sorted_data[size // 2 - 1] + sorted_data[size // 2]) / 2
    else:
        return sorted_data[size // 2]


def quartile(data: tuple) -> list:
    """Quartile"""
    sorted_data = sorted(data)
    size = len(sorted_data)
    Q1 = median(sorted_data[:size // 2])
    if size % 2 == 0:
        Q2 = median(sorted_data[size // 2:])
    else:
        Q2 = median(sorted_data[size // 2 + 1:])
    return [Q1, Q2]


def var(data: tuple) -> int:
    """Variance"""
    moy = mean(data)
    return sum((x - moy) ** 2 for x in data) / len(data)


def std(data: tuple) -> int:
    """Standard deviation"""
    return var(data) ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    """Function that takes a list of integers and a list of strings as args."""

    try:
        assert all(isinstance(a, int) for a in args), "args are not int"

        functions = {
            'var': var,
            'std': std,
            'mean': mean,
            'median': median,
            'quartile': quartile,
        }

        for key, value in kwargs.items():
            if len(args) == 0:
                print("ERROR")
            elif len(args) < 2:
                print("Please provide at least two numbers")
            elif value in functions:
                print(f"{value} : {functions[value](args)}")

    except AssertionError as msg:
        print(f"Assertion Error: {msg}")
