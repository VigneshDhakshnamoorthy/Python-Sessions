import numpy as np

board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                 [0, 0, 3, 0, 1, 0, 0, 8, 0],
                 [9, 0, 0, 8, 6, 3, 0, 0, 5],
                 [0, 5, 0, 0, 9, 0, 6, 0, 0],
                 [1, 3, 0, 0, 0, 0, 2, 5, 0],
                 [0, 0, 0, 0, 0, 0, 0, 7, 4],
                 [0, 0, 5, 2, 0, 6, 3, 0, 0]]

blanks = np.where(board == 0)


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i  != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8 :
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


print_board(board)

