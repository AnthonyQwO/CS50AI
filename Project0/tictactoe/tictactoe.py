"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
INF = 0xffffffff

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xt = 0 
    Ot = 0 

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xt += 1
            elif board[i][j] == O:
                Ot += 1

    if Xt == Ot:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ret = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                ret.add((i, j))
    return ret


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    chess = player(board)
    ret = copy.deepcopy(board)
    ret[action[0]][action[1]] = chess
    return ret


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    res = utility(board)
    if res == 1:
        return X
    if res == -1:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    hasWinner = utility(board)
    if hasWinner != 0:
        return True
    move = actions(board)
    if len(move) <= 0:
        return True
    return False


def flag(chess):
    if chess == X:
        return 1
    return -1


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return flag(board[0][0])
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return flag(board[0][0])
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return flag(board[0][0])
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return flag(board[2][0])
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return flag(board[2][0])
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return flag(board[0][2])
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return flag(board[1][0])
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return flag(board[0][1])
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board using alpha-beta pruning.
    """
    chess = player(board)
    alpha = -INF
    beta = INF
    ret = (0, (0, 0))

    if chess == X:
        ret = (-INF, (0, 0))
        for action in actions(board):
            val = minValue(result(board, action), alpha, beta)
            if val > alpha:
                alpha = val
                ret = (val, action)
    elif chess == O:
        ret = (INF, (0, 0))
        for action in actions(board):
            val = maxValue(result(board, action), alpha, beta)
            if val < beta:
                beta = val
                ret = (val, action)

    return ret[1]

def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -INF
    for action in actions(board):
        v = max(v, minValue(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)

    return v

def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = INF
    for action in actions(board):
        v = min(v, maxValue(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)

    return v
