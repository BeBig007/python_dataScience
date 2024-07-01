from abc import ABC, abstractmethod


class Character(ABC):
    """Character is an Abstract Base Class for Game of Thrones characters"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Sets the character's is_alive attribute to False"""
        pass


class Stark(Character):
    """Stark class inherits from Character"""

    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor for Stark"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Sets the Stark's is_alive attribute to False"""
        self.is_alive = False
