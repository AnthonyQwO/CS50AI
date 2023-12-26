import sys
import tictactoe as ttt


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    chess = player(board)
    ret = (0,(0,0))
    if chess == X:
        ret = (-INF,(0,0))
        for action in actions(board):
            ret = max(ret, (minValue(result(board,action)), action))
    elif chess == O:
        ret = (INF,(0,0))
        for action in actions(board):
            ret = min(ret, (maxValue(result(board,action)), action))
    return ret[1]


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -INF
    for action in actions(board):
        ret = minValue(result(board,action))
        v = max(v, ret)
    return v


def minValue(board):
    if terminal(board):
        return utility(board)
    v = INF
    for action in actions(board):
        ret = maxValue(result(board,action))
        v = min(v, ret)
    return v


def minValue(board, pruning):
    if terminal(board):
        return utility(board)
    v = INF
    for action in actions(board):
        ret = maxValue(result(board,action), v)
        if ret <= pruning:
            return v
        v = min(v, ret)
    return v

def printboard(board):
    for i in board:
        for j in i:
            if j == None:
                print("#",end="")
            else:
                print(j,end="")
        print()
    print()


board = [[ttt.O, ttt.X, ttt.O],
        [ttt.EMPTY, ttt.X, ttt.EMPTY],
        [ttt.X, ttt.EMPTY, ttt.EMPTY]]
"""
print(board)
while not ttt.terminal(board):
    board = ttt.result(board,ttt.minimax(board))
    print(board)
"""
print(ttt.minimax(board))

