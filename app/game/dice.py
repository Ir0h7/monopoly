import random


class Dice:
    def __init__(self):
        self.__first = 0
        self.__second = 0
        self.__casino = 0

    @property
    def point(self) -> int: return self.__first + self.__second

    @property
    def casino(self) -> int: return self.__casino

    @property
    def is_double(self) -> bool: return self.__first == self.__second

    def roll(self) -> None:
        self.__first = random.randint(1, 6)
        self.__second = random.randint(1, 6)

    def casino_roll(self) -> None:
        self.__casino = random.randint(1, 6)

    def print_dice(self) -> None:
        print(self.__first, '+', self.__second, '=', self.point)