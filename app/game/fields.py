from abc import ABC, abstractmethod
from player import Player


class Field(ABC):
    def __init__(self, number: int, img: str):
        self.number = number
        self.img = img

    @property
    def color(self):
        return '000000'

    @abstractmethod
    def print_field(self):
        print(self.number, self.img, self.color)


class UnPurchasedField(Field):
    def __init__(self, number, img):
        super().__init__(number, img)

    @abstractmethod
    def print_field(self):
        super().print_field()


class ChanceField(UnPurchasedField):
    def print_field(self):
        super().print_field()


class PoliceField(UnPurchasedField):
    def print_field(self):
        super().print_field()


class StartField(UnPurchasedField):
    def print_field(self):
        super().print_field()


class PrisonField(UnPurchasedField):
    def print_field(self):
        super().print_field()


class TaxField(UnPurchasedField):
    def print_field(self):
        super().print_field()


class CasinoField(UnPurchasedField):
    def print_field(self):
        super().print_field()


class PurchasedField(Field):
    def __init__(self,
                 number: int, img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, img)
        self.cost = cost
        self.name = name
        self.redemption_cost = redemption_cost
        self.pledge_cost = pledge_cost
        self.owner = Player()

    @property
    def color(self):
        return self.owner.color

    @abstractmethod
    def print_field(self):
        super().print_field()
        print(self.name, self.cost, self.redemption_cost, self.pledge_cost)


class MonopolyField(PurchasedField):
    def __init__(self,
                 number: int, img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int,
                 rents: tuple[int], upgrade_cost: int, monopoly_type: int):
        super().__init__(number, img, name, cost, redemption_cost, pledge_cost)
        self.upgrade_cost = upgrade_cost
        self.rents = rents
        self.monopoly_type = monopoly_type

    def print_field(self):
        super().print_field()
        print(*self.rents, '\n', self.upgrade_cost, self.pledge_cost)


class CarField(PurchasedField):
    def __init__(self,
                 number: int, img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()


class UnbelievableXXXField(PurchasedField):
    def __init__(self,
                 number: int, img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()
