import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array from start to end.

    Args:
        family (list): List of lists.
        start (int): Start index.
        end (int): End index.

    Returns:
        list: Sliced list of lists.
    """
    try:
        assert all(isinstance(i, list) for i in family), "The input must be a list of lists"
        assert isinstance(start, int) and isinstance(end, int), "Start and end must be integers"
        assert all(len(i) ==  2 for i in family), "All sublists must have the same length."
        array = numpy.array(family)
        print(f"My shape is : {array.shape}")

        new_array = array[start: end]
        print(f"My new shape is : {new_array.shape}")
        return new_array.tolist()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return []
