from typing import List
import random

def board_generation() -> List[list]:
    """
    Generates a game board of 16 x 4 size,
    i.e. two dimensional list (array) of 'g's,
    'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],\
    [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],\
    [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],\
    [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    ball_list = [0, 'w', 'g']
    board = []
    for _ in range(16):
        board.append([0,0,0,0])
    level = 3
    column = 0
    w_count = 16
    g_count = 16
    while column < 16:
        while level >= 0:
            if level == 3:
                index = random.randint(0,len(ball_list)-1)
                board[column][level] = ball_list[index]
            else:
                if board[column][level+1] == 0:
                    board[column][level+1] = 0
                else:
                    index = random.randint(0,len(ball_list)-1)
                    board[column][level] = ball_list[index]
            if board[column][level] == 'w':
                w_count -= 1
            elif board[column][level] == 'g':
                g_count -= 1

            if w_count == 0:
                try:
                    ball_list.remove('w')
                except ValueError:
                    pass
            if g_count == 0:
                try:
                    ball_list.remove('g')
                except ValueError:
                    pass
            level -= 1
        level = 3
        column += 1
    print(board)
    return board


def winning_combination(board: List[list]) -> bool:
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions
    if there is winning combination or False if not.

    >>> winning_combination([[0, 'g', 'g', 'g'], \
[0, 'g', 'w', 'w'], [0, 0, 'g', 'g'],[0, 0, 0, 0], \
[0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], \
[0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], \
['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 0], \
[0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], \
['g', 'g', 'g', 'w'], [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], \
[0, 0, 0, 'w'], ['w', 'g', 'g', 'g'], ['w', 'w', 'g', 'w'], \
[0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 0], \
[0, 'g', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], \
[0, 'g', 'w', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], \
[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w'], \
['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], \
[0, 0, 'g', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], \
[0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], \
[0, 0, 0, 'g'], ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], \
[0, 0, 0, 'w'], ['w', 'g', 'w', 'g'], [0, 0, 'w', 'w'], \
[0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0, 0, 0], \
[0, 0, 0, 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], \
[0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], \
[0, 0, 'w', 'g'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], \
[0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g', 'g'], \
[0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], \
['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], \
['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([[0, 0, 'g', 'g'], [0, 0, 0, 'g'], \
[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], \
['w', 'w', 'g', 'g'], ['w', 'w', 'g', 'g'], ['w', 'g', 'g', 'w'], \
[0, 'g', 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], \
[0, 0, 0, 'g'], [0, 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], \
[0, 0, 'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], \
[0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], \
[0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], \
[0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], \
['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], \
[(3, 14), (3, 15), (3, 0), (3, 1)], \
[(3, 15), (3, 0), (3, 1), (3, 2)]])
    """
    result_list =[]
    for i in range(16):
        for j in range(4):
            row_index1 = i
            row_index2 = (i+1) % 16
            row_index3 = (i+2) % 16
            row_index4 = (i+3) % 16
            if board[i][j] != 0:
                if j == 0:
                    if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                        result_list.append([(j, i), (j+1, i), (j+2, i), (j+3, i)])
                    if board[row_index1][j] == board[row_index2][j+1] \
                        == board[row_index3][j+2] == board[row_index4][j+3]:
                        result_list.append([(j,row_index1), (j+1,row_index2), \
                            (j+2, row_index3), (j+3, row_index4)])
                elif j == 3:
                    if board[row_index1][j] == board[row_index2][j-1] \
                        == board[row_index3][j-2] == board[row_index4][j-3]:
                        result_list.append([(j, row_index1), (j-1, row_index2), \
                            (j-2, row_index3), (j-3, row_index4)])
                if board[row_index1][j] == board[row_index2][j] == \
                    board[row_index3][j] == board[row_index4][j]:
                    result_list.append([(j, row_index1), (j,row_index2), \
                            (j,row_index3), (j,row_index4)])
    if len(result_list) > 0:
        return (True, result_list)
    return False        
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
