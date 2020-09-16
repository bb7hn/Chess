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


def getPiecePoint(piece, x, y):
    if piece == "Q":
        return 9 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "R":
        return 5 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "N" or piece == "B":
        return 3 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "P":
        return 1 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "q":
        return -9 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "r":
        return -5 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "n" or piece == "b":
        return -3 + getCurrentPointOfTable(x, y, piece)*0.33
    elif piece == "p":
        return -1 + getCurrentPointOfTable(x, y, piece)*0.33
    else:
        return 0


def CountIsolatedPawn(board):
    pawnb = 0
    pawnw = 0
    isolatedw = 0
    isolatedb = 0
    for i in range(8):
        for j in range(8):
            if board[j][i] == "p":
                pawnb += 1
            if board[j][i] == "P":
                pawnw += 1
        if pawnw < 1:
            isolatedw += 1
        if pawnb < 1:
            isolatedb += 1
        pawnb = 0
        pawnw = 0
    return (isolatedw - isolatedb)*0.5


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
            if board[i][j] != ".":
                if board[i][j].lower():
                    score += getPiecePoint(board[i][j], i, j)
                else:
                    score -= getPiecePoint(board[i][j], i, j)
    if Board.result() == "1-0":
        score += 200
    elif Board.result() == "0-1":
        score -= 200
    score -= CountDoubledPawn(board)
    score -= CountIsolatedPawn(board)
    return score


"""f(p) = 200(K-K')
       + 9(Q-Q')
       + 5(R-R')
       + 3(B-B' + N-N')
       + 1(P-P')
       - 0.5(D-D' + S-S' + I-I')
       + 0.1(M-M') + ..."""


def getTotalScore(board, turn):
    totalscore = 0
    for i in range(8):
        for j in range(8):
            if turn == True and board[i][j].isupper():
                totalscore += getCurrentPointOfTable(i, j, board[i][j])
            elif turn == False and board[i][j].islower():
                totalscore -= getCurrentPointOfTable(i, j, board[i][j])
    return totalscore


def findBestMoveWhite(Board, board):  # For White
    legalMoves = getLegalMoves(Board)

    """numOfMoveToRemove = math.floor(len(legalMoves)*0.2)
    for i in range(numOfMoveToRemove):
        del legalMoves[random.randint(0, len(legalMoves)-1)]"""

    bestScore = -99999999
    bestMove = ""
    if legalMoves == "Check Mate!":
        print("Check Mate!")
        return 0
    for move in legalMoves:
        Board.push_san(move)
        score = minimax(Board, board, 0, False)
        Board.pop()
        print(score, "            ", move)
        if score > bestScore:
            bestScore = score
            bestMove = move
    Board.push_san(bestMove)


def findBestMove(Board, board):
    legalMoves = getLegalMoves(Board)

    """numOfMoveToRemove = math.floor(len(legalMoves)*0.2)
    for i in range(numOfMoveToRemove):
        del legalMoves[random.randint(0, len(legalMoves)-1)]"""

    bestScore = -99999999
    bestMove = ""
    if legalMoves == "Check Mate!":
        print("Check Mate!")
        return 0
    for move in legalMoves:
        Board.push_san(move)
        score = minimax(Board, board, 0, -99999999, 99999999, True)
        Board.pop()
        print(score, "            ", move)
        if score > bestScore:
            bestScore = score
            bestMove = move
    Board.push_san(bestMove)


def minimax(Board, board, depth, alpha, beta, isMaximizing):
    legalMoves = getLegalMoves(Board)
    if legalMoves == 0:
        return 0
    if Board.is_checkmate == True or depth >= 3:
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
            score += getTotalScore(board, True)*0.7
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
            score += getTotalScore(board, False)*0.7
            Board.pop()
            board = boardToStr(Board)
            bestScore = min(score, bestScore)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return bestScore


def makemove(Board):
    print("Legal Moves:\n", Board.legal_moves)
    print("Your move:")
    move = input()
    islegal = 0
    legalMoves = getLegalMoves(Board)
    for moves in legalMoves:
        if moves == move:
            Board.push_san(move)
            islegal = 1
            break
    if islegal == 0:
        print("move is not legal")


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
    drawGameState(screen, board)
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        if Board.is_checkmate():
            print("Check Mate!")
        if Board.is_repetition(20):
            print("Draw")
        if(Board.turn):
            #print("Legal Moves:\n", Board.legal_moves)
            findBestMove(Board, board)
            board = boardToStr(Board)
            """findBestMoveWhite(Board, board)"""
        else:
            print("Legal Moves:\n", Board.legal_moves)
            makemove(Board)
            board = boardToStr(Board)
        drawGameState(screen, board)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, board):
    drawBoard(screen)
    drawPieces(screen, board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("#D2691E")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
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


fen = "8/1n1k2n1/1p1p1p1p/pPpPpPpP/P1P1P1P1/6Q1/8/R3K2R b KQ - 0 1"
Board = chess.Board()
board = boardToStr(Board)
main(Board, board)
