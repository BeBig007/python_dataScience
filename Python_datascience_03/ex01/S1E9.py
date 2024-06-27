from abc import ABC, abstractmethod


class Character(ABC):
    """Character is an Abstract Base Class
    Args:
        first_name (str): The first name of the character
        is_alive (bool, opt): Whether the character is alive. Defaults: True
    """
    def __init__(self, first_name, is_alive=True):
        """Constructor
        Args:
            first_name (str): first name of the character
            is_alive (bool, opt): Whether the character is alive Defaults: True
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Sets the character's is_alive attribute to False"""
        pass


class Stark(Character):
    """Stark class inherits from Character
    Args:
        Character (ABC): Abstract Base Class
    """

    def __init__(self, first_name, is_alive = True):
        """Constructor for Stark
        Args:
            first_name (str): first name of the Stark character
            is_alive (bool, opt): Whether the character is alive Defaults: True
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Sets the Stark's is_alive attribute to False"""
        self.is_alive = False
