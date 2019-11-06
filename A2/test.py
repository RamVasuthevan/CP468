import sudoku_board


def testBoard(n: int = 1):
    """
    Takes in a number m. Prints the nth board, the post AC-3 domain set and the post AC-3 board

    Args:
        board: Board to be printed
        empty_value: Values to be printed if cell is empty
    Print:
        nth
    """
    board = sudoku_board.load_file(n=n)[n-1]
    sudoku_board.pretty_print_board(board)

    constraints = sudoku_board.create_constraint_set()
    domains = sudoku_board.create_domain_set(board)

    ret = sudoku_board.AC3(sudoku_board.ALL_CELLS, constraints, domains)

    if not ret:
        print("AC-3 has identified that there is not an solution")

    else:
        if not sudoku_board.vaildSolve(board, sudoku_board.domains2Board(ret)):
            print("THIS IS NOT A VAILD SOLUTION (AC-3 is not implemented correctly)")

        if not sudoku_board.solved(ret):
            print(f"SOLVED {sudoku_board.solved(ret)}")
            for key, val in ret.items():
                print(f"{key} : {val}")

        sudoku_board.pretty_print_domain(ret)

def find_partial_solution():
    """
    Find the first Sudoku can't be fully solved by AC-3. Prints the domains and board

    Args:
    Print:
        Prints the domains and board
    """
    BOARDS_TO_CHECK = 900

    boards = sudoku_board.load_file(n=BOARDS_TO_CHECK)
    constraints = sudoku_board.create_constraint_set()
    ret = sudoku_board.AC3(sudoku_board.ALL_CELLS, constraints, sudoku_board.create_domain_set(boards.pop(0)))

    while boards and sudoku_board.solved(ret):
        ret = sudoku_board.AC3(sudoku_board.ALL_CELLS, constraints, sudoku_board.create_domain_set(boards.pop(0)))

    if not sudoku_board.solved(ret):
        for key, val in ret.items():
            print(f"{key} : {val}")
        sudoku_board.pretty_print_domain(ret)
    else:
        print(f"Tried to find a partial solution amongst {BOARDS_TO_CHECK} board and didn't find one")

#testBoard(15)
#find_partial_solution()