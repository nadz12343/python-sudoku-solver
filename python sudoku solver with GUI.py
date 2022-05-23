from pydoc import classname
import time
import tkinter as tk
from threading import Thread
from random import randint
from tkinter.constants import ANCHOR, N


def isArrayValid(array):
    r = [1,2,3,4,5,6,7,8,9]
    occuranceOfCurrentNum = 0 
    for i in r: # for value, i check if it is found within every entry in the array
        occuranceOfCurrentNum = 0
        for j in range(len(array)):
            if i == array[j]:
                occuranceOfCurrentNum += 1 #if occurance of i is found then increment
            if occuranceOfCurrentNum >= 2: #not valid when true
                return False
    return True

#checks if the row passed in as an argument is correct and follows the contraints
def isRowValid(row):
    return isArrayValid(row)

#checks if the column passed in as an argument is correct and follows the contraints
def isColValid(board, colNum):
    col = []
    for i in range(9):
        col.append(board[i][colNum])
    return isArrayValid(col)

#checks if the grid passed in as an argument is correct and follows the contraints
def isGridValid(board, gridNum):
    a = []
    rowRange = (0,3)  #when gridNum is either 0,1,2 then the row ranges from 0-2, not including 3
    
    if gridNum >=3 and gridNum <=5: #when gridNum is in this range then column range differs
        colRange = (3, 5)
    elif gridNum >=6 and gridNum <=8:
        colRange = (6, 9)
    else:
        colRange = (0, 3)

    for i in range(gridNum % 3): #gridNum % 3 gives us the correct row, even when gridNum gets larger than 3
        rowRange = (rowRange[0]+3, rowRange[1]+3)
    
    for row in range(rowRange[0], rowRange[1]):
        for col in range(colRange[0], colRange[1]):
            a.append(board[row][col] )
    return isArrayValid(a)

#checks if the whole sudoku board passed in as an argument is correct and follows the contraints
def isBoardValid(board):
    #check if all rows are valid
    for row in range(9):
        if not isRowValid(board[row]): #call the gridvalid function to determine validity
            return False  
    for grid in range(9):
        if not isGridValid(board, grid): #call the gridvalid function to determine validity
            return False
    for col in range(9):
        if not isColValid(board, col): #call the gridvalid function to determine validity
            return False
    return True #if reached to this stage then we carry on executing the code


def findEmptyCell(board):
    for i in range(9):
        if board[i] == -1:
            return i
    return -1

def findAllEmptyCell(board):
    a = []
    for i in range(9):
        if board[i] == -1:
            a.append(i)
    return a


def solveSudoku(board, row = 0):

    if row == 9: #when there is no rows to traverse, then return True, meaning that sudoku is solved
        return True
    loc = findEmptyCell(board[row]) #find the current empty location of the sudoku puzzle
    if loc == -1: #no empty cell and thus traverse the next row
        return solveSudoku(board, row+1)
    for i in range(1, 10): #at the current empty cell put a 1-9 until
        board[row][loc] = i
        time.sleep(.01)
        c[row][loc].set(str(board[row][loc])) #,,
        if isBoardValid(board) == True: #true -> move to the next empty cell, false -> assign current location to -1, incases where we will immediatly backtrack, so that finding an empty cell will perform correclty
            if solveSudoku(board, row): #true when the future empty cells are valid, false -> assign current empty cell to -1 (empty)
                return True
            else:
                board[row][loc] =-1 #incases where future empty cells are not valid, and thus we need to assign the current location back to -1, so that findEmptyLocation will work correctly.
                time.sleep(.01)
                c[row][loc].set("    ") #,,
        else:
            board[row][loc] = -1 #
            time.sleep(.01)
            c[row][loc].set("    ") #,,
    return False #backtracking purposes


##### EXAMPLE CASES ########
    
board = [
[5, -1, -1,  -1, 9, -1,  6, 7, 2],
[-1, 2, -1,  1, -1, -1,  5, 4, -1],
[-1, 4, -1,  5, 2,   7,  8, 3, -1],

[4,9, -1,   3,8,-1,  -1,5,-1],
[-1,1, 8,   -1,-1,-1,  -1,-1,-1],
[7, -1,-1,  -1,-1,-1,  -1,-1,4],

[-1,-1,2,   -1, 3,-1,   4, -1, 5],
[-1,8,5,    2, -1, -1,  7, -1, 3],
[3,7,-1,    -1, 5,-1,  -1, 2, 8],
]


# solved example
s_board = [
[5,  3, 1,  8, 9, 4,  6, 7, 2],
[8,  2, 7,  1, 6, 3,  5, 4, 9],
[6,  4, 9,  5, 2, 7,  8, 3, 1],

[4,9, 6,   3,8, 2,  1,5,7],
[2,1, 8,   4,7,5,  3, 9,6],
[7, 5,3,  9,1, 6,  2,8,4],

[9,6,2,   7, 3, 8,   4, 1, 5],
[1,8,5,    2, 4, 9,  7, 6, 3],
[3,7,4,    6, 5, 1,  9, 2, 8],
]


b = [[3,8,5,-1,-1,-1,-1,-1,-1], [9,2,1,-1,-1,-1,-1,-1,-1], [6,4,7,-1,-1,-1,-1,-1,-1],
     [-1, -1, -1,1,2,3,-1,-1,-1], [-1,-1,-1,7,8,4,-1,-1,-1], [-1,-1,-1,6,9,5,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,8,7,3], [-1,-1,-1, -1, -1, -1,9, 6, 2], [-1, -1, -1, -1, -1, -1, 1, 4, 5 ]
]

p = [[2, -1, -1, 5, -1, 7, -1, -1, -1], 
     [-1, -1, 6, 2, 3, -1, 1, -1, -1], 
     [7, 5, 3, 6, -1, -1, -1, 4, 8],
     [-1, -1, -1, 8, -1, -1, 4, 5, 1], 
     [3, -1 ,-1, -1, 6, -1, 9, -1, 2],
     [-1, 8, 5, -1, 2, -1, -1, 3, -1],
     [5, -1, 1, -1, -1, 9, 6, -1, -1],
     [-1, 4, 9, 7, -1, -1, -1, -1, 3],
     [8, 2, 7, -1, -1, 6, -1, 9, -1]
]

##### THIS IS THE SECTION OF CODE THAT CREATES THE GUI DISPLAYS THE BACKTRACKING PROCESS #####

#GUI initialisation
win = tk.Tk(className = "Sudoku Solver")
win.geometry("500x600")
win.resizable(False,False)

a= [[None for i in range(9)] for i in range(9)]
c= [[tk.StringVar() for i in range(9)] for j in range(9)]

#setting up the sudoku board using the 'board' array for the values.
for i in range(9):
    for j in range(9):
        if board[i][j] == -1:
            c[i][j].set("    ")
        else:
            c[i][j].set(str(board[i][j]))

for i in range(9):
    for j in range(9):
        a[i][j] = tk.Label(textvariable= c[i][j],  borderwidth= 1, padx=10, pady=10, relief="solid").grid(row=i, column=j, padx= (10,20), pady = 10)
l = tk.DoubleVar()
w = tk.Scale(win, variable= l,).grid(row= 9, column=5, )


# concurrency/threading is executed here, it simultanously solves the puzzle and displays the intermediaries in the GUI
def solve_the_puzzle():
    solveSudoku(board)
    print(board)
    print("complete")
    time.sleep(30)

r = Thread(target=solve_the_puzzle)
r.start()  

win.mainloop()
