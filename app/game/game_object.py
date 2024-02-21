from abc import ABC, abstractmethod


class Player:
    def __init__(self, player_id: int = None, name: str = None, color: str = None):
        self.__player_id = player_id
        self.__name = name
        self.__bal = 15000
        self.__own_list = []
        self.__pledge_list = []
        self.__position = 0
        self.__color = color

    @property
    def player_id(self): return self.__player_id

    @property
    def name(self): return self.__name

    @property
    def bal(self): return self.__bal

    @property
    def own_list(self): return self.__own_list

    @property
    def pledge_list(self): return self.__pledge_list

    @property
    def position(self): return self.__position

    @property
    def color(self): return self.__color

    @property
    def list_of_monopoly(self):
        type_own = []
        monopoly_type_count = []
        for i in self.__own_list:
            if i.__monopoly_type in type_own:
                monopoly_type_count[type_own.index(i.__monopoly_type)] += 1
            else:
                type_own.append(i.__monopoly_type)
                monopoly_type_count.append([1, i.count])
        list_of_monopoly = []
        for i in range(len(type_own)):
            if monopoly_type_count[i][0] == monopoly_type_count[i][1]:
                list_of_monopoly.append(type_own[i])
        return list_of_monopoly

    def purchase_field(self, field: 'PurchasedField') -> bool:
        if isinstance(field, PurchasedField) and field.cost <= self.__bal and field.owner is None:
            self.__own_list.append(field)
            field.owner = self
            self.__bal -= field.cost
            return True
        return False

    def pledge_field(self, field: 'PurchasedField') -> bool:
        if field in self.__own_list:
            self.__own_list.remove(field)
            self.__pledge_list.append(field)
            field.pledge()
            self.__bal += field.pledge_cost
            return True
        return False

    def redemption_field(self, field: 'PurchasedField') -> bool:
        if field in self.__pledge_list and self.__bal >= field.redemption_cost:
            self.__pledge_list.remove(field)
            self.__own_list.append(field)
            field.redemption()
            self.__bal -= field.redemption_cost
            return True
        return False

    def move(self, field_size: int) -> (int, int):
        self.__position = (self.__position + 1) % field_size
        return 1, 0


class Field(ABC):
    def __init__(self, number: int, label: tuple[str], img: str):
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
    def get_label(self, player: Player):
        pass


class UnPurchasedField(Field):
    def __init__(self, number: int, img: str, label: tuple[str]):
        super().__init__(number, label, img)

    @abstractmethod
    def print_field(self):
        super().print_field()

    def get_label(self, player: Player):
        pass


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
        self.__cost = cost
        self.__name = name
        self.__redemption_cost = redemption_cost
        self.__pledge_cost = pledge_cost
        self.__is_pledged = False
        self.owner = None

    @property
    def cost(self): return self.__cost

    @property
    def name(self): return self.__name

    @property
    def redemption_cost(self): return self.__redemption_cost

    @property
    def pledge_cost(self): return self.__pledge_cost

    @property
    def is_pledged(self): return self.__is_pledged

    def pledge(self): self.__is_pledged = True

    def redemption(self): self.__is_pledged = False

    @property
    def color(self):
        if self.owner is not None:
            return self.owner.color
        return '000000'

    def get_label(self, player: Player) -> str:
        if self.owner is None:
            return self.label[0].format(player.name, self.__name, self.__cost)
        elif self.owner is player:
            return self.label[1].format(player.name)
        elif self.__is_pledged:
            return self.label[3].format(player.name, self.owner.name)
        else:
            return self.label[3].format(player.name, self.owner.name, self.rent)

    @abstractmethod
    def print_field(self):
        super().print_field()
        print(self.__name,
              self.__cost,
              self.__redemption_cost,
              self.__pledge_cost,
              self.__is_pledged,
              self.owner.name if self.owner is not None else None)

    @abstractmethod
    def rent(self):
        pass


class MonopolyField(PurchasedField):
    def __init__(self,
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int,
                 rents: tuple[int], upgrade_cost: int, monopoly_type: int, monopoly_count: int):
        super().__init__(number, label, img, name, cost, redemption_cost, pledge_cost)
        self.__upgrade_cost = upgrade_cost
        self.__rents = rents
        self.__monopoly_type = monopoly_type
        self.__monopoly_count = monopoly_count

    @property
    def upgrade_cost(self): return self.__upgrade_cost

    @property
    def monopoly_type(self): return self.__monopoly_type

    @property
    def monopoly_count(self): return self.__monopoly_count

    @property
    def rent(self):
        return 0

    def print_field(self):
        super().print_field()
        print(*self.__rents, '\n', self.__upgrade_cost)


class CarField(PurchasedField):
    def __init__(self,
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, label, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()

    @property
    def rent(self):
        return 0


class UnbelievableXXXField(PurchasedField):
    def __init__(self,
                 number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(number, label, img, name, cost, redemption_cost, pledge_cost)

    def print_field(self):
        super().print_field()

    @property
    def rent(self):
        return 0
