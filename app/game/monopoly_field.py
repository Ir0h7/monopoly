from app.game import PurchasedField
from app.game import Dice


class MonopolyField(PurchasedField):
    def __init__(self,
                 dice: Dice, number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int,
                 rents: tuple[int], upgrade_cost: int, monopoly_type: int, monopoly_count: int):
        super().__init__(dice, number, label, img, name, cost, redemption_cost, pledge_cost)
        self.__upgrade_cost = upgrade_cost
        self.__rents = rents
        self.__monopoly_type = monopoly_type
        self.__monopoly_count = monopoly_count
        self.__level = 0

    @property
    def upgrade_cost(self): return self.__upgrade_cost

    @property
    def monopoly_type(self): return self.__monopoly_type

    @property
    def monopoly_count(self): return self.__monopoly_count

    @property
    def rent(self):
        if self.__level != 0:
            return self.__rents[self.__level]
        elif self.__monopoly_type in self.owner.list_of_monopoly:
            return self.__rents[0] * 2

    def print_field(self):
        super().print_field()
        print(*self.__rents, '\n', self.__upgrade_cost)
