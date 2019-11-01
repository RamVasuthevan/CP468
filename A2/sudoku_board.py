import numpy as np

def print_formated_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(j<len(board[i])-1):
                print(board[i][j], end = ", ")
            else:
                print(board[i][j])

# load_file() loads sudoku.csv which contains sudoku game boards with solutions
# returns ndarray of shape (9,9) dtype = np.int8
def load_file():
    fv = open("A2\sudoku.csv")
    title = fv.readline()

    first_sudoku_and_solution = fv.readline()
    sudoku_num_list = first_sudoku_and_solution.strip().split(",")[0]

    sudoku_board = np.zeros((9,9), dtype= np.int8)


    for i in range(len(sudoku_num_list)):
        sudoku_board[i//9][i%9] = sudoku_num_list[i]

    return sudoku_board

