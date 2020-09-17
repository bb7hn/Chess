import pygame as p
import chess
# GUI PART
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]


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


def loadImages():
    pieces = ['b', 'k',  'n', 'p', 'q', 'r']
    for piece in pieces:
        IMAGES[piece+"b"] = p.transform.scale(p.image.load(
            "img/" + piece + "b.png"), (SQ_SIZE, SQ_SIZE))
        IMAGES[piece+"w"] = p.transform.scale(p.image.load(
            "img/" + piece + "w.png"), (SQ_SIZE, SQ_SIZE))


def main(board, turn):
    p.init()
    p.display.set_caption('Chess')
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    loadImages()
    running = True
    sqSelected = ()  # no square is selected, keep track of the last click of the user(tuple: (row, col))
    # keep track of player clicks (two tuples: [(6,5), (4,4)])
    playerClicks = []
    while running:
        board = boardToStr(Board)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if e.button == 3:
                    sqSelected = ()
                    playerClicks = []
                    move = ""
                    continue
                location = p.mouse.get_pos()  # (x, y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (col, row):  # the user clicked the same square twice
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    # append for both 1st and 2nd clicks
                    playerClicks.append(sqSelected)
                    piece2 = board[row][col]

                if len(playerClicks) == 2:  # after the 2nd click
                    move = createMoveFromPosition(playerClicks, piece2)
                    print(playerClicks)
                    print(move)
                    Board.push_san(move)
                    sqSelected = ()
                    playerClicks = []
                    move = ""

        drawGameState(screen, board, sqSelected)
        clock.tick(MAX_FPS)
        p.display.flip()


def createMoveFromPosition(playerClicks, piece2):
    print(playerClicks)
    board = boardToStr(Board)
    posOne = playerClicks[0]  # 1st clicked position
    posTwo = playerClicks[1]
    piece = board[posOne[0]][posOne[1]]  # 2nd clicked position
    if piece.upper() == "P":  # eğer piyonsa
        if piece2 != ".":  # eğer taş varsa
            move = LETTERS[posOne[1]]+"x" + \
                LETTERS[posTwo[1]] + \
                str(8-posTwo[0])  # yeme hamlesi yap
        else:  # eğer taş yoksa
            # ve hamle taşla aynı düzlemde değilse
            move = LETTERS[posOne[1]]+str(8-posTwo[0])
    if piece.upper() == "R":
        if piece2 != ".":  # eğer taş varsa
            move = "R"+"x"+LETTERS[posTwo[1]] + \
                str(8-posTwo[0])  # yeme hamlesi yap
        else:
            move = "R"+LETTERS[posOne[1]]+str(8-posTwo[0])
    if piece.upper() == "N":
        if piece2 != ".":  # eğer taş varsa
            move = ""+"x"+LETTERS[posTwo[1]] + \
                str(8-posTwo[0])  # yeme hamlesi yap
        else:
            move = "N"+LETTERS[posTwo[1]]+str(8-posTwo[0])
    if piece.upper() == "B":
        if piece2 != ".":  # eğer taş varsa
            move = "B"+"x"+LETTERS[posTwo[1]] + \
                str(8-posTwo[0])  # yeme hamlesi yap
        else:
            move = "B"+LETTERS[posTwo[1]]+str(8-posTwo[0])
    if piece.upper() == "K":
        if piece2 != ".":  # eğer taş varsa
            move = "K"+"x"+LETTERS[posTwo[1]] + \
                str(8-posTwo[0])  # yeme hamlesi yap
        else:
            move = "K"+LETTERS[posOne[1]]+str(8-posTwo[0])
    if piece.upper() == "Q":
        if piece2 != ".":  # eğer taş varsa
            move = "Q"+"x"+LETTERS[posTwo[1]] + \
                str(8-posTwo[0])  # yeme hamlesi yap
        else:
            move = "Q"+LETTERS[posOne[1]]+str(8-posTwo[0])
    return move


def drawGameState(screen, board, sqSelected):
    drawBoard(screen, sqSelected)
    drawPieces(screen, board)


def drawBoard(screen, sqSelected):
    colors = [p.Color("white"), p.Color("#5f5f5f"), p.Color("#377b8c")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if sqSelected == (r, c):
                color = colors[2]
            else:
                color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != ".":
                if piece.isupper():
                    screen.blit(
                        IMAGES[piece.lower()+"w"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    screen.blit(
                        IMAGES[piece.lower()+"b"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


fen = "rnbqk1nr/pppp1ppp/3b4/4p3/8/8/PPPPPPPP/RNBQKBNR b KQkq - 5 4"
Board = chess.Board(fen)
board = boardToStr(Board)
main(board, Board.turn)
