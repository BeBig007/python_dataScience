import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class with name, surname, active, login and id attributes.
    The login is the first letter of the name and the surname.
    The id is a random string of 15 lowercase letters."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Set the login attribute."""
        self.login = self.name[0] + self.surname
