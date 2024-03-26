from abc import abstractmethod
from app.game import Field
from app.game import Dice


class PurchasedField(Field):
    def __init__(self,
                 dice: Dice, number: int, label: tuple[str], img: str,
                 name: str, cost: int, redemption_cost: int, pledge_cost: int):
        super().__init__(dice, number, label, img)
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

    def get_label(self, player: 'Player') -> str:
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

    def short_print_field(self):
        owner = self.owner.name if self.owner is not None else 'None'
        print(self.number, self.__name, self.__cost, owner)