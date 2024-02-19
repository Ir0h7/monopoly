from player import Player
from rules import *


class Game:
    def __init__(self, count_players: int, players_id: tuple[int], colors: tuple[int]):
        self.players = []
        self.game_field = []
        for i in range(count_players):
            self.players.append(Player(players_id[i], colors[i]))
        for i in range(len(fields)):
            field_type = fields[i][0]
            self.game_field.append(field_types[field_type](i, *fields[i][1:]))

    def print_game_field(self):
        for i in self.game_field:
            i.print_field()
