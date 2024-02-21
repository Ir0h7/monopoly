import rules
from app.game import Player


class Game:
    def __init__(self, count_players: int, players_id: tuple[int], names: tuple[str], colors: tuple[int]):
        self.players = []
        self.game_field = []
        for i in range(count_players):
            self.players.append(Player(players_id[i], names[i], colors[i]))
        self.cur_player = self.players[0]
        for i in range(len(rules.FIELDS)):
            field_type = rules.FIELDS[i][0]
            self.game_field.append(rules.FIELD_TYPES[field_type](i, rules.LABELS[field_type], *rules.FIELDS[i][1:]))

    def print_game_field(self):
        for i in self.game_field:
            i.print_field()

    def move(self, move_type: str, data: tuple = ()):
        if move_type == 'roll':
            data = tuple([len(self.game_field)])
            t = rules.MOVE_TYPES[move_type](self.cur_player, *data)
            return t, self.game_field[self.cur_player.position].get_label(self.cur_player)
        elif move_type == 'purchase':
            data = tuple([self.game_field[self.cur_player.position]])
        return rules.MOVE_TYPES[move_type](self.cur_player, *data)
