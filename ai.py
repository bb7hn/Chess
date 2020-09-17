import math
import random
import chess
from os import system
import pygame as p


def oppositeBoolean(boolean):
    if(boolean):
        return False
    else:
        return True


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


def getLegalMoves(Board):
    if Board.is_checkmate():
        return 0
    legalMoves = str(Board.legal_moves.count)
    legalMoves = legalMoves[legalMoves.index(
        "(")+1:legalMoves.index(")")].replace(" ", "").split(",")
    return legalMoves


def getCurrentPointOfTable(x, y, stone):
    king = [[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0],
            [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
            [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]]

    rook = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
            [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]]

    knight = [[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
              [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
              [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
              [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
              [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
              [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
              [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
              [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]

    pawn = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
            [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
            [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
            [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
            [0.0, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
            [0.5, 1.0, 1.0, -2.0, -2.0,  1.0, 1.0, 0.5],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    queen = [[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
             [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
             [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
             [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
             [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
             [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
             [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
             [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]

    bishop = [[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
              [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
              [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
              [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
              [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
              [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
              [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
              [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]

    if stone == "R":
        return rook[x][y]
    elif stone == "N":
        return knight[x][y]
    elif stone == "B":
        return bishop[x][y]
    elif stone == "Q":
        return queen[x][y]
    elif stone == "K":
        return king[x][y]
    elif stone == "P":
        return pawn[x][y]
    elif stone == "r":
        return -rook[7-x][7-y]
    elif stone == "n":
        return -knight[7-x][7-y]
    elif stone == "b":
        return -bishop[7-x][7-y]
    elif stone == "q":
        return -queen[7-x][7-y]
    elif stone == "k":
        return -king[7-x][7-y]
    elif stone == "p":
        return -pawn[7-x][7-y]
    else:
        return 0


def getPiecePoint(piece):
    if piece == "Q":
        return 9
    elif piece == "R":
        return 5
    elif piece == "N" or piece == "B":
        return 3
    elif piece == "P":
        return 1
    elif piece == "q":
        return -9
    elif piece == "r":
        return -5
    elif piece == "n" or piece == "b":
        return -3
    elif piece == "p":
        return -1
    else:
        return 0


def CountDoubledPawn(board):
    pawnb = 0
    pawnw = 0
    scoreb = 0
    scorew = 0
    for i in range(8):
        for j in range(8):
            if board[j][i] == "p":
                pawnb += 1
            if board[j][i] == "P":
                pawnw += 1
        if pawnw >= 2:
            scorew += pawnw/2
        if pawnb >= 2:
            scoreb += pawnb/2
        pawnb = 0
        pawnw = 0
    return (scorew - scoreb)*0.5


def Evaluation(Board, board):  # + point for white - point for black
    score = 0
    for i in range(8):
        for j in range(8):
            score += getPiecePoint(board[i][j])
    if Board.result() == "1-0":
        score += 200
    elif Board.result() == "0-1":
        score -= 200
    return score


"""f(p) = 200(K-K')
       + 9(Q-Q')
       + 5(R-R')
       + 3(B-B' + N-N')
       + 1(P-P')
       - 0.5(D-D' + S-S' + I-I')
       + 0.1(M-M') + ..."""


def takeSecond(elem):
    return elem[1]


def takeBestMoveRandomly(moveList):
    bestMoveScore = moveList[0][1]  # take best move's score
    bestMoveList = []
    for move in moveList:
        if move[1] == bestMoveScore:  # if move score is equal best score
            bestMoveList.append(move)  # take it to the list
    # return the list
    return bestMoveList[random.randint(0, len(bestMoveList)-1)][0]

# sort the move list from higher point to lower point


def findBestMove(Board, board, color):
    legalMoves = getLegalMoves(Board)
    moveList = []
    """numOfMoveToRemove = math.floor(len(legalMoves)*0.2)
    for i in range(numOfMoveToRemove):
        del legalMoves[random.randint(0, len(legalMoves)-1)]"""
    if color:
        bestScore = -99999999
    else:
        bestScore = 99999999
    bestMove = ""
    if legalMoves == "Check Mate!":
        print("Check Mate!")
        return 0
    for move in legalMoves:
        Board.push_san(move)
        score = minimax(Board, board, 0, -99999999, 99999999, False)
        Board.pop()
        print(score, "            ", move)
        if color:
            if score >= bestScore:
                bestScore = score
                bestMove = move
                moveList.append((bestMove, bestScore))
        else:
            if score <= bestScore:
                bestScore = score
                bestMove = move
                moveList.append((bestMove, bestScore))

    if color:  # if White's turn sort from higher to lower
        moveList.sort(key=takeSecond, reverse=True)
    else:  # if Black's turn sort from lower to higher with that way move choiser function chose the best move for each side in White's turn best move for white in Black's turn worst move for White
        moveList.sort(key=takeSecond, reverse=False)

    bestMove = takeBestMoveRandomly(moveList)

    Board.push_san(bestMove)
    # print(Board.fen())


def minimax(Board, board, depth, alpha, beta, isMaximizing):
    legalMoves = getLegalMoves(Board)
    if legalMoves == 0:
        return 0
    if Board.is_checkmate == True or depth >= DEPTH:
        return Evaluation(Board, board)

    if isMaximizing == True:
        bestScore = -9999999
        for move in legalMoves:
            if move == "":
                continue
            Board.push_san(move)
            board = boardToStr(Board)
            score = Evaluation(Board, board)
            score += minimax(Board, board, depth+1, alpha, beta, False)
            Board.pop()
            board = boardToStr(Board)
            bestScore = max(score, bestScore)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return bestScore
    else:
        bestScore = 999999
        for move in legalMoves:
            if move == "":
                continue
            Board.push_san(str(move))
            board = boardToStr(Board)
            score = Evaluation(Board, board)
            score += minimax(Board, board, depth+1, alpha, beta, True)
            Board.pop()
            board = boardToStr(Board)
            bestScore = min(score, bestScore)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return bestScore


def printBoard(Board):
    print("  A B C D E F G H")
    boardStr = boardToStr(Board)
    lineNum = 8
    for line in boardStr:
        lineStr = str(line)
        lineStr = lineStr[1:]
        lineStr = lineStr[:len(lineStr)-2]
        lineStr = lineStr.replace("'", "")
        lineStr = lineStr.replace(",", "")
        print(str(lineNum), lineStr)
        lineNum -= 1


# GUI PART
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h"]


def loadImages():
    pieces = ['b', 'k',  'n', 'p', 'q', 'r']
    for piece in pieces:
        IMAGES[piece+"b"] = p.transform.scale(p.image.load(
            "img/" + piece + "b.png"), (SQ_SIZE, SQ_SIZE))
        IMAGES[piece+"w"] = p.transform.scale(p.image.load(
            "img/" + piece + "w.png"), (SQ_SIZE, SQ_SIZE))


def main(Board, board):
    p.init()
    p.display.set_caption('Chess')
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    loadImages()
    running = True
    sqSelected = ()
    col = -1
    # no square is selected, keep track of the last click of the user(tuple: (row, col))
    row = -1
    # keep track of player clicks (two tuples: [(6,5), (4,4)])
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        board = boardToStr(Board)
        turn = Board.turn
        board = boardToStr(Board)
        drawGameState(screen, board, sqSelected)
        clock.tick(MAX_FPS)
        p.display.flip()
        if Board.is_checkmate():
            print("Check Mate!")
        if Board.is_repetition(20):
            print("Draw")
        if(turn):
            #print("Legal Moves:\n", Board.legal_moves)
            findBestMove(Board, board, turn)  # White's move
            board = boardToStr(Board)
        else:
            findBestMove(Board, board, turn)  # Black's move
            board = boardToStr(Board)
        """elif e.type == p.MOUSEBUTTONDOWN:

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

                if turn and piece2.islower() and len(playerClicks) < 1:
                    sqSelected = ()
                    playerClicks = []
                elif turn == False and piece2.isupper() and len(playerClicks) < 1:
                    sqSelected = ()
                    playerClicks = []
                if len(playerClicks) == 2:  # after the 2nd click
                    move = createMoveFromPosition(playerClicks, piece2)
                    makeMove(Board, move)
                    print(move)
                    sqSelected = ()
                    playerClicks = []
                    move = """

        board = boardToStr(Board)
        drawGameState(screen, board, sqSelected)
        clock.tick(MAX_FPS)
        p.display.flip()


def createMoveFromPosition(playerClicks, piece2):
    board = boardToStr(Board)
    move = ""
    print(playerClicks)
    posOne = playerClicks[0]  # 1st clicked position
    posTwo = playerClicks[1]  # 2nd clicked position
    piece = board[posOne[0]][posOne[1]]
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
            move = "N"+"x"+LETTERS[posTwo[1]] + \
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
            move = "Q"+LETTERS[posTwo[1]]+str(8-posTwo[0])
    return move


def drawGameState(screen, board, sqSelected):
    drawBoard(screen, sqSelected)
    drawPieces(screen, board)


def drawBoard(screen, sqSelected):
    colors = [p.Color("white"), p.Color("#5f5f5f"), p.Color("#377b8c")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if sqSelected != (-1, -1):
                if sqSelected == (r, c):
                    color = colors[2]
                else:
                    color = colors[(r+c) % 2]
            else:
                color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            BoardLetters(screen, r, c)


def BoardLetters(screen, r, c):
    font = p.font.SysFont('segoescript', 15, bold=20)
    if r == 0 and c == 0:
        screen.blit(font.render('8', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 1 and c == 0:
        screen.blit(font.render('7', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 2 and c == 0:
        screen.blit(font.render('6', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 3 and c == 0:
        screen.blit(font.render('5', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 4 and c == 0:
        screen.blit(font.render('4', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 5 and c == 0:
        screen.blit(font.render('3', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 6 and c == 0:
        screen.blit(font.render('2', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 7 and c == 0:
        screen.blit(font.render('1', True, (0, 0, 0)),
                    (c*SQ_SIZE, r*SQ_SIZE-6))
    if r == 7 and c == 0:
        screen.blit(font.render('A', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 1:
        screen.blit(font.render('B', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 2:
        screen.blit(font.render('C', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 3:
        screen.blit(font.render('D', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 4:
        screen.blit(font.render('E', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 5:
        screen.blit(font.render('F', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 6:
        screen.blit(font.render('G', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))
    if r == 7 and c == 7:
        screen.blit(font.render('H', True, (0, 0, 0)),
                    (c*SQ_SIZE-2, r*SQ_SIZE+42))


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


def makeMove(Board, move):
    islegal = 0
    legalMoves = getLegalMoves(Board)
    for moves in legalMoves:
        if move in moves:
            Board.push_san(moves)
            islegal = 1
            break
    if islegal == 0:
        print("move is not legal")
    else:
        print(Board.fen())


DEPTH = 3
fen = "r1b2k1r/ppp2ppp/2p5/8/2B5/4N3/PPPn1PPP/R4RK1 w - - 0 1"
Board = chess.Board(fen)
board = boardToStr(Board)
main(Board, board)
