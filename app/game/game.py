import rules
from app.game import Player


class Game:
    def __init__(self, count_players: int, players_id: tuple[int], names: tuple[str], colors: tuple[int]):
        self.players = []
        self.game_field = []
        for i in range(count_players):
            self.players.append(Player(players_id[i], names[i], colors[i]))
        self.cur_player = self.players[0]
        for i in range(len(rules.fields)):
            field_type = rules.fields[i][0]
            self.game_field.append(rules.field_types[field_type](i, rules.labels[field_type], *rules.fields[i][1:]))

    def print_game_field(self):
        for i in self.game_field:
            i.print_field()

    def move(self, move_type: str, data: tuple = ()):
        if move_type == 'roll':
            data = tuple([len(self.game_field)])
            t = rules.move_types[move_type](self.cur_player, *data)
            return t, self.game_field[self.cur_player.position].get_label(self.cur_player)
        elif move_type == 'purchase':
            data = tuple([self.game_field[self.cur_player.position]])
        return rules.move_types[move_type](self.cur_player, *data)
