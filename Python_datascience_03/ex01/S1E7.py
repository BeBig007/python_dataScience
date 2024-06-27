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

    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return super().__repr__()

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

    def die(self):
        """Sets the Lannister's is_alive attribute to False"""
        self.is_alive = False

    # decorator
    def create_lannister():
        print()
