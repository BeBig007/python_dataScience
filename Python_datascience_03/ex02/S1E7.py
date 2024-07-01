from S1E9 import Character


class Baratheon(Character):
    """Baratheon class inherits from Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Returns a string representation of the object"""
        return str(self)

    def die(self):
        """Sets the Baratheon's is_alive attribute to False"""
        self.is_alive = False


class Lannister(Character):
    """Lannister class inherits from Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Returns a string representation of the object"""
        return str(self)

    def die(self):
        """Sets the Lannister's is_alive attribute to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Creates a Lannister character"""
        return cls(first_name, is_alive)
