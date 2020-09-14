import chess
    
from os import system

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
        return 9
    elif piece == "r":
        return 5
    elif piece == "n" or piece == "b":
        return 3
    elif piece == "p":
        return 1
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
            scorew += 1
        if pawnb >= 2:
            scoreb += 1
        pawnb = 0
        pawnw = 0
    return scorew - scoreb


def Evaluation(Board, board):  # + point for white - point for black
    score = 0
    for i in range(8):
        for j in range(8):
            if board[i][j].isupper():
                score += getPiecePoint(board[i][j])
            else:
                score -= getPiecePoint(board[i][j])
    if(Board.is_checkmate):
        score += 200
    score -= 0.5*CountDoubledPawn(board)
    score += 0.1*int(Board.legal_moves.count())
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
                totalscore += getCurrentPointOfTable(i, j, board[i][j])
    return totalscore

import math
import random
def findBestMoveWhite(Board, board): # Beyaz
    legalMoves = getLegalMoves(Board)

    numOfMoveToRemove = math.floor(len(legalMoves)*0.2)
    for i in range (numOfMoveToRemove):
        del legalMoves[random.randint(0,len(legalMoves)-1)]
        
    bestScore = -99999999
    bestMove = ""
    if legalMoves == "Check Mate!":
        print("Check Mate!")
        return 0
    for move in legalMoves:
        Board.push_san(move)
        score = minimax(Board, board, 0, True, 9999999, -9999999)
        Board.pop()
        #print(score, "     ", move)
        if score > bestScore:
            bestScore = score
            bestMove = move

    Board.push_san(bestMove)
    
def findBestMove(Board, board): # Siyah
    legalMoves = getLegalMoves(Board)
    
    numOfMoveToRemove = math.floor(len(legalMoves)*0.2)
    for i in range (numOfMoveToRemove):
        del legalMoves[random.randint(0,len(legalMoves)-1)]
        
    legalMoves = getLegalMoves(Board)
    bestScore = 99999999
    bestMove = ""
    if legalMoves == "Check Mate!":
        print("Check Mate!")
        return 0
    for move in legalMoves:
        Board.push_san(move)
        score = minimax(Board, board, 0, False, 9999999, -9999999)
        Board.pop()
        #print(score, "     ", move)
        if score < bestScore:
            bestScore = score
            bestMove = move

    Board.push_san(bestMove)


def minimax(Board, board, depth, isMaximizing, alpha, beta):
    legalMoves = getLegalMoves(Board)
    if legalMoves == 0:
        return 0
    if Board.is_checkmate == True or depth >= 10:
        return getTotalScore(board, oppositeBoolean(isMaximizing))

    if isMaximizing == True:
        bestScore = -9999999
        for move in legalMoves:
            if move == "":
                continue
            Board.push_san(move)
            board = boardToStr(Board)
            score = minimax(Board, board, depth+1, False, alpha, beta) + \
                Evaluation(Board, board)
            Board.pop()
            board = boardToStr(Board)
            bestScore = max(score, bestScore)
            alpha = max(alpha, bestScore)
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
            score = minimax(Board, board, depth+1, True, alpha, beta) + \
                Evaluation(Board, board)
            Board.pop()
            board = boardToStr(Board)
            bestScore = min(score, bestScore)
            beta = min(score, bestScore)
            if beta <= alpha:
                break
        return bestScore


Board = chess.Board()
board = boardToStr(Board)


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



while 1:
    if Board.is_checkmate():
        print("Check Mate!")
        break
    if Board.is_repetition(20):
        print("Draw")
        break
    if(Board.turn):
        #print("Legal Moves:\n", Board.legal_moves)
        #findBestMoveWhite(Board, board)
        #board = boardToStr(Board)
        #print("E(x) = ", Evaluation(Board, board))
        makemove(Board)
        board = boardToStr(Board)
        print("E(x) = ", Evaluation(Board, board))
    else:
        #print("Legal Moves:\n", Board.legal_moves)
        findBestMove(Board, board)
        board = boardToStr(Board)
        #print("E(x) = ", Evaluation(Board, board))
    system('cls')
    printBoard(Board)
    

