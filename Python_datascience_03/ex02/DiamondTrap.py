from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Args:
        Baratheon ( ):
        Lannister ( ):
    """

    def __init__(self, first_name, is_alive=True, eyes='blue', hairs='pink'):
        """_summary_
        Args:
            first_name ( ):
            is_alive (bool, optional): . Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs

    @property
    def eyes(self):
        print("eyes Getting value...")
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        print("eyes Setting value...")
        self._eyes = color

    @property
    def hairs(self):
        print("hairs Getting value...")
        return self._hairs

    @hairs.setter
    def hairs(self, color):
        print("hairs Setting value...")
        self._hairs = color
