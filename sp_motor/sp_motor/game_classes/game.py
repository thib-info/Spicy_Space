
class game:
    def __init__(self, conf):
        self.players = conf["players"]
        self.list_systems = conf["map"]
        self.turn = conf["turn"]

    def next_turn(self):
        self.turn += 1





