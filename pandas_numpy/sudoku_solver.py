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




def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i  != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8 :
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")



def possible(row,column,number):
    global board
    for i in range(0,9):
        if board[row][i] == number:
            return False    
    for j in range(0,9):
        if board[j][column] == number:
            return False
    row0 = (row//3)*3
    column0 = (column//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[row0+i][column0+j] == number:
                return False
    return True 
           
def solve():    
    global board
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0
                return
    print_board(board)

solve()





