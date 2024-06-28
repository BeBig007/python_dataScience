from S1E9 import Character


class Baratheon(Character):
    """Baratheon class inherits from Character
    Args:
        Character (ABC): Abstract Base Class
    """

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon
        Args:
            first_name (str): first name of the Baratheon character
            is_alive (bool, opt): Whether the character is alive Defaults: True
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return str(self)

    def die(self):
        """Sets the Baratheon's is_alive attribute to False"""
        self.is_alive = False


class Lannister(Character):
    """Lannister class inherits from Character
    Args:
        Character (ABC): Abstract Base Class
    """

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister
        Args:
            first_name (str): first name of the Lannister character
            is_alive (bool, opt): Whether the character is alive Defaults: True
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return str(self)

    def die(self):
        """Sets the Lannister's is_alive attribute to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
