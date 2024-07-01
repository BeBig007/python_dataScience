from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class inherits from Baratheon and Lannister"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for King"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        """Sets the eyes attribute to new_eyes"""
        self.eyes = new_eyes

    def set_hairs(self, new_hairs):
        """Sets the hairs attribute to new_hairs"""
        self.hairs = new_hairs

    def get_eyes(self):
        """Returns the eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """Returns the hairs attribute"""
        return self.hairs

    # @property
    # def eyes(self):
    #     return self.eyes

    # @eyes.setter
    # def eyes(self, new_eyes):
    #     self._eyes = new_eyes

    # @property
    # def hairs(self):
    #     return self.hairs

    # @hairs.setter
    # def hairs(self, new_hairs):
    #     self._hairs = new_hairs
