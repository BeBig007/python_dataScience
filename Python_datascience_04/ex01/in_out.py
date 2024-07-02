
def square(x: int | float) -> int | float:
    """square function"""
    return x * x


def pow(x: int | float) -> int | float:
    """power function"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer function"""

    if not isinstance(x, (int, float)):
        raise ValueError("arg must be a int/float")

    if function not in [globals()[name] for name in ['pow', 'square']]:
        raise ValueError("function argument must be either pow or square")

    count = 0
    curent_result = x

    def inner() -> float:
        """inner function"""
        nonlocal count, curent_result
        curent_result = function(curent_result)
        count += 1
        return curent_result
    return inner
