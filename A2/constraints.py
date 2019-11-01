import sudoku_board

def list_of_constrained_variables(x_coord, y_coord):
    variables = []
    
    for x in range(9):
        for y in range(9):
            if (x == x_coord) or (y == y_coord) or (x_coord / 3 == x / 3 and y_coord / 3 == y / 3):
                variables.append((x,y))

    #don't worry about adding the coord we are at before, just remove it at the end
    variables.remove((x_coord,y_coord))

    return variables


def create_constraint_set(board):
    #  variable_address = 
    #  key = (variable_address_1, variable_address_2)
    #  value = [constraint_litteral] (value it can not be)
    constraints = dict()
    for x in range(9):
        for y in range(9):
            constraints[(x,y)] = []
    
    #iterate through each cell in the board and if necessary add constraints to the constraints dict
    for i, row in enumerate(board):
        for j, constraint_litteral in enumerate(row):
            constrained_list = list_of_constrained_variables(i,j)
            if(constraint_litteral != 0):
                for cell in constrained_list:
                    constraints[cell].append(constraint_litteral)
    
    return constraints


def _test_():
    board = sudoku_board.load_file()
    cs = create_constraint_set(board)
    for i in cs:
        print("key: ",i, "value: ", cs[i])


    