
def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""

    assert isinstance(limit, int) and limit >= 0, \
        "limit must be a positive int"

    count = 0
    value = None

    def callLimiter(function):
        """Inner function that limits the number of times
            a function can be called."""

        def limit_function(*args, **kwds):
            """Function that limits the number of times a function"""
            nonlocal count, value
            if count < limit:
                value = function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
            count += 1
            return value
        return limit_function
    return callLimiter
