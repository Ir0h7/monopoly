class Player:
    def __init__(self, player_id: int = None, color: str = None):
        if player_id is not None:
            self.id = player_id
            self.bal = 15000
            self.list_of_own = []
            self.field_number = 0
            self.color = color
        else:
            self.color = '000000'
