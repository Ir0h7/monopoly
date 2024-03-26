from app.game import Dice, PurchasedField


class Player:
    def __init__(self, dice: Dice, player_id: int = None, name: str = None, color: str = None):
        self.__dice = dice
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
        for field in self.__own_list:
            if field.monopoly_type in type_own:
                monopoly_type_count[type_own.index(field.monopoly_type)] += 1
            else:
                type_own.append(field.monopoly_type)
                monopoly_type_count.append([1, field.count])
        list_of_monopoly = []
        for i in range(len(type_own)):
            if monopoly_type_count[i][0] == monopoly_type_count[i][1]:
                list_of_monopoly.append(type_own[i])
        return list_of_monopoly

    def purchase_field(self, field: PurchasedField) -> bool:
        if isinstance(field, PurchasedField) and field.cost <= self.__bal and field.owner is None:
            self.__own_list.append(field)
            field.owner = self
            self.__bal -= field.cost
            return True
        return False

    def pledge_field(self, field: PurchasedField) -> bool:
        if field in self.__own_list:
            self.__own_list.remove(field)
            self.__pledge_list.append(field)
            field.pledge()
            self.__bal += field.pledge_cost
            return True
        return False

    def redemption_field(self, field: PurchasedField) -> bool:
        if field in self.__pledge_list and self.__bal >= field.redemption_cost:
            self.__pledge_list.remove(field)
            self.__own_list.append(field)
            field.redemption()
            self.__bal -= field.redemption_cost
            return True
        return False

    def move(self, field_size: int): self.__position = (self.__position + self.__dice.point) % field_size
