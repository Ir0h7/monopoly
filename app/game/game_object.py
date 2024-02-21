from abc import ABC, abstractmethod
import typing

PurchasedField = typing.NewType('PurchasedField', None)


class Player:
    def __init__(self, player_id: int = None, name: str = None, color: str = '0000000'):
        self.id = player_id
        self.name = name
        self.bal = 15000
        self.list_of_own = []
        self.list_of_pledge = []
        self.position = 0
        self.color = color

    def purchase_field(self, field: PurchasedField) -> bool:
        if isinstance(field, PurchasedField) and field.cost <= self.bal and field.owner.id is None:
            self.list_of_own.append(field)
            field.owner = self
            self.bal -= field.cost
            return True
        return False

    def pledge_field(self, field: PurchasedField) -> bool:
        if field in self.list_of_own:
            self.list_of_own.remove(field)
            self.list_of_pledge.append(field)
            field.is_pledged = True
            self.bal += field.pledge_cost
            return True
        return False

    def redemption_field(self, field: PurchasedField) -> bool:
        if field in self.list_of_pledge and self.bal >= field.pledge_cost:
            self.list_of_pledge.remove(field)
            self.list_of_own.append(field)
            field.is_pledged = False
            self.bal -= field.pledge_cost
            return True
        return False

    def move(self, field_size: int) -> (int, int):
        self.position = (self.position + 1) % field_size
        return 1, 0


class Field(ABC):
    def __init__(self, number: int, label: tuple[str], img: str):
        self.number = number
        self.label = label
        self.img = img

    @property
    def color(self):
        return '000000'

    @abstractmethod
    def print_field(self):
        print(self.number, self.img, self.color)

    @abstractmethod
    def get_label(self):
        return self.label[0]


class UnPurchasedField(Field):
    def __init__(self, number: int, img: str, label: tuple[str]):
        super().__init__(number, label, img)

    @abstractmethod
    def print_field(self):
        super().print_field()

    def get_label(self):
        super().get_label()


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
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, label, img)
        self.cost = cost
        self.name = name
        self.redemption_cost = redemption_cost
        self.pledge_cost = pledge_cost
        self.is_pledged = False
        self.owner = Player()

    def get_label(self, player: Player) -> str:
        if self.owner.id is None:
            return self.label[0].format(player.name, self.name, self.cost)
        elif self.owner is player:
            return self.label[1].format(player.name)
        elif self.is_pledged:
            return self.label[3].format(player.name, self.owner.name)
        else:
            return self.label[3].format(player.name, self.owner.name, self.get_rent())

    @property
    def color(self):
        return self.owner.color

    @abstractmethod
    def print_field(self):
        super().print_field()
        print(self.name, self.cost, self.redemption_cost, self.pledge_cost, self.is_pledged, self.owner.name)

    @abstractmethod
    def get_rent(self):
        pass


class MonopolyField(PurchasedField):
    def __init__(self,
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int,
                 rents: tuple[int], upgrade_cost: int, monopoly_type: int):
        super().__init__(number, label, img, name, cost, redemption_cost, pledge_cost)
        self.upgrade_cost = upgrade_cost
        self.rents = rents
        self.monopoly_type = monopoly_type

    def print_field(self):
        super().print_field()
        print(*self.rents, '\n', self.upgrade_cost, self.pledge_cost)

    def get_rent(self):
        super().get_rent()


class CarField(PurchasedField):
    def __init__(self,
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, label, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()

    def get_rent(self):
        super().get_rent()


class UnbelievableXXXField(PurchasedField):
    def __init__(self,
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, label, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()

    def get_rent(self):
        super().get_rent()
