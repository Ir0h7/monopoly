from abc import abstractmethod
from app.game import Field, Dice


class UnPurchasedField(Field):
    def __init__(self, dice: Dice, number: int, img: str, label: tuple[str]):
        super().__init__(dice, number, label, img)

    @abstractmethod
    def print_field(self):
        super().print_field()

    def get_label(self, player: 'Player'):
        pass