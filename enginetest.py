import chess


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def boardToStr(board):
    lstboard = list(str(board).replace(" ", ","))
    result = listToString(lstboard)
    rSplit = result.split('\n')

    l = []

    for item in rSplit:
        subl = []
        for num in item.split(','):
            subl.append(str(num))
        l.append(subl)

    return l


class GameState():
    def __init__(self):
        self.Board = chess.Board()
        self.board = boardToStr(self.Board)
        self.whiteToMove = self.Board.turn
        self.moveLog = []
        return self.board
