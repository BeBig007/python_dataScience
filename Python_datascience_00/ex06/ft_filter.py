
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))

# if __name__ == "__main__":
#     nums = [0, 1, 2, 3, 4, 5]
#     evens = ft_filter(lambda x: x % 2 == 0, nums)
#     print(list(evens))  # Output: [0, 2, 4]

#     mixed = [0, 1, False, True, '', 'Hello']
#     trues = ft_filter(None, mixed)
#     print(list(trues))  # Output: [1, True, 'Hello']
