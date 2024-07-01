class calculator:
    """A simple calculator class."""

    def __init__(self, val) -> None:
        """Constructor for the calculator class."""
        self.val = val

    def __add__(self, object) -> None:
        """Adds a value to the list of values."""
        self.val = [x + object for x in self.val]
        print(self.val)

    def __mul__(self, object) -> None:
        """Multiplies a value to the list of values."""
        self.val = [x * object for x in self.val]
        print(self.val)

    def __sub__(self, object) -> None:
        """Subtracts a value to the list of values."""
        self.val = [x - object for x in self.val]
        print(self.val)

    def __truediv__(self, object) -> None:
        """Divides a value to the list of values."""
        if object == 0:
            raise ValueError("Cannot divide by 0")
        self.val = [x / object for x in self.val]
        print(self.val)

    def __repr__(self):
        """Returns a string representation of the Calculator object."""
        return f"Calculator({self.val})"
