class Battle_Ship_Game():
    """Creates a battle ship game"""

    width = 10
    height = 10

    def __init__(self):
        self.board = [[0 for x in range(10)] for y in range(10)]
        self.board[5][5] = "X"
        self.board[5][4] = "X"
        self.board[5][6] = "X"

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Battle Ship | w: {}, h: {} >""".format(self.width, self.height)


def hit_ship(x, y):
    """Returns bool if the x, y coordinate hit a ship"""

    if GAME.board[x][y] == "X":
        return True

    return False

HEIGHT = 10
WIDTH = 10
GAME = Battle_Ship_Game()
