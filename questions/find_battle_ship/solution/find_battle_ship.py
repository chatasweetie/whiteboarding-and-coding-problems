from battleship import GAME, WIDTH, HEIGHT


def find_ship():
    """Returns the coordinates of a three unit size ship

    time: O(mn)
    space: 0(1)
    """

    for w in range(WIDTH):
        for h in range(HEIGHT):
            if GAME.board[w][h] == "X":
                if GAME.board[w+1][h] == "X":
                    return [[w, h], [w+1, h], [w+2, h]]
                if GAME.board[w][h+1] == "X":
                    return [[w, h], [w, h+1], [w, h+2]]

    return False
