import rules
from app.game import Player, Dice


class Game:
    @classmethod
    @property
    def cmd_dict(cls):
        upgrade = rules.get_methods_dict(cls, '_' + cls.__name__ + '__cmd_', '_upgrade')
        deposit = rules.get_methods_dict(cls, '_' + cls.__name__ + '__cmd_', '_deposit')
        stop = rules.get_methods_dict(cls, '_' + cls.__name__ + '__cmd_', '_stop')
        roll = rules.get_methods_dict(cls, '_' + cls.__name__ + '__cmd_', '_roll')
        res = upgrade | deposit | stop | roll
        return res

    @classmethod
    @property
    def upgrade_cmd_list(cls):
        res = rules.get_methods_list(cls, '_' + cls.__name__ + '__cmd_', '_upgrade')
        for i in range(len(res)):
            res[i] = res[i][11:-8]
        return res

    @classmethod
    @property
    def deposit_cmd_list(cls):
        res = rules.get_methods_list(cls, '_' + cls.__name__ + '__cmd_', '_deposit')
        for i in range(len(res)):
            res[i] = res[i][11:-8]
        return res

    @classmethod
    @property
    def stop_cmd_list(cls):
        res = rules.get_methods_list(cls, '_' + cls.__name__ + '__cmd_', '_stop')
        for i in range(len(res)):
            res[i] = res[i][11:-5]
        return res

    @classmethod
    def is_start(cls, cmd: str): return cmd in cls.upgrade_cmd_list or cmd in cls.deposit_cmd_list or cmd == 'roll'

    @classmethod
    def is_end(cls, cmd: str): return cmd in cls.stop_cmd_list or cmd in cls.deposit_cmd_list

    def __init__(self, count_players: int, players_id: tuple[int], names: tuple[str], colors: tuple[int]):
        self.dice = Dice()
        self.phase = 'start'
        self.double_count = 0
        self.players = []
        self.game_field = []
        for i in range(count_players):
            self.players.append(Player(self.dice, players_id[i], names[i], colors[i]))
        self.cur_player_id = 0
        for i in range(len(rules.FIELDS)):
            field_type = rules.FIELDS[i][0]
            self.game_field.append(rules.FIELD_TYPES[field_type](self.dice, i, rules.LABELS[field_type], *rules.FIELDS[i][1:]))
        print(*self.cmd_dict)

    @property
    def cur_player(self): return self.players[self.cur_player_id]

    def is_valid(self, cmd: str): return self.is_start(cmd) if self.phase == 'start' else self.is_end(cmd)

    def print_game_field(self, index: int = None):
        if index is not None:
            print(self.game_field[index])
        else:
            for i in self.game_field:
                i.print_field()

    def short_print_game_field(self):
        for i in self.game_field:
            i.short_print_field()

    def command(self, cmd: str, data: dict = None):
        return self.cmd_dict[cmd](self, data) if self.is_valid(cmd) else 'соси'

    def __cmd_roll(self, data: dict = None):
        self.dice.roll()
        self.double_count += self.dice.is_double
        if self.double_count == 3:
            self.__stop_method(True)
            return 'соси'
        else:
            self.phase = 'end'
            self.cur_player.move(len(self.game_field))
            return self.game_field[self.cur_player.position].get_label(self.cur_player)

    def __cmd_up_upgrade(self, data: dict = None):
        pass

    def __cmd_redemption_upgrade(self, data: dict = None):
        return self.cur_player.pledge_field(self.game_field[data['field']])

    def __cmd_pledge_deposit(self, data: dict = None):
        return self.cur_player.pledge_field(self.game_field[data['field']])

    def __cmd_downgrade_deposit(self, data: dict = None):
        pass

    def __cmd_trade_deposit(self, data: dict = None):
        pass

    def __stop_method(self, force: bool = False):
        self.phase = 'start'
        if not self.dice.is_double or force:
            self.cur_player_id = (self.cur_player_id + 1) % len(self.players)
            self.double_count = 0

    def __cmd_purchase_stop(self, data: dict = None):
        self.cur_player.purchase_field(self.game_field[self.cur_player.position])
        self.__stop_method()

    def __cmd_skip_stop(self, data: dict = None):
        self.__stop_method()

    def __cmd_rent_stop(self, data: dict = None):
        self.__stop_method()
