from app.game import PurchasedField
from app.game import Dice


class CarField(PurchasedField):
    def __init__(self,
                 dice: Dice, number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(dice, number, label, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()

    @property
    def rent(self):
        return 0
