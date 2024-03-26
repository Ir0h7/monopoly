from abc import ABC, abstractmethod
from app.game import Dice


class Field(ABC):
    def __init__(self, dice: Dice, number: int, label: tuple[str], img: str):
        self.__dice = dice
        self.__number = number
        self.__label = label
        self.__img = img

    @property
    def number(self): return self.__number

    @property
    def label(self): return self.__label

    @property
    def img(self): return self.__img

    @property
    def color(self):
        return '000000'

    @abstractmethod
    def print_field(self):
        print(self.__number, self.__img, self.color)

    @abstractmethod
    def get_label(self, player: 'Player'):
        pass