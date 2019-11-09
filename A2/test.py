import sudoku_board
import numpy as np


def testBoard(n: int = 1):
    """
    Takes in a number n. Prints the nth board, the post AC-3 domain set and the post AC-3 board

    Args:
        board: Board to be printed
        empty_value: Values to be printed if cell is empty
    Print:
        nth
    """
    board = sudoku_board.load_file(n=n)[n-1]
    print("Sudoku Board Initialized:")
    sudoku_board.pretty_print_board(board)
    print()

    constraints = sudoku_board.create_constraint_set()
    domains = sudoku_board.create_domain_set(board)

    ret = sudoku_board.AC3( constraints, domains)

    if not ret:
        print("AC-3 has identified that there is no solution")

    else:
        if not sudoku_board.validSolve(board, sudoku_board.domains2Board(ret)):
            print("THIS IS NOT A VAILD SOLUTION (AC-3 was not implemented correctly)")

        else:
            print(f"SOLVED = {sudoku_board.solved(ret)}")
#             for key, val in ret.items():
#                 print(f"{key} : {val}")
                
        
        print("Last found arc consistency")
        sudoku_board.pretty_print_domain(ret)
        print()

def find_partial_solution():
    """
    Find the first Sudoku can't be fully solved by AC-3. Prints the domains and board

    Args:
    Print:
        Prints the domains and board
    """
    BOARDS_TO_CHECK = 900
    failed = 0
    btSolved = 0
    
    
    
    boards = sudoku_board.load_file(n=BOARDS_TO_CHECK)
    constraints = sudoku_board.create_constraint_set()
    ret = sudoku_board.AC3( constraints, sudoku_board.create_domain_set(boards.pop(0)))
    boardChecked = 1
    
    while boards:
        ret = sudoku_board.AC3( constraints, sudoku_board.create_domain_set(boards.pop(0)))
        boardChecked += 1

        if not sudoku_board.solved(ret):
            print(f"\nSudoku board {boardChecked} was unable to be solved by AC-3 algorithm")
            
            board = sudoku_board.load_file(n=boardChecked)[boardChecked-1]
            print(f"\nSudoku Board {boardChecked} initial values:")
            sudoku_board.pretty_print_board(board)
            
            print(f"\nLast found arc consistency for board {boardChecked}:")
            sudoku_board.pretty_print_domain(ret)
            
#             print(f"\nLast found cell domains for board {boardChecked}:")
#             for key, val in ret.items():
#                 print(f"{key} : {val}")
                
            print(f"\nAttempting to solve board {boardChecked} with backtracking")
            btracked = sudoku_board.backtracking_search(constraints, ret)
            
            if type(btracked) == np.ndarray:
                print(f"\nSolution to board {boardChecked} was found using backtracking: ")
                btSolved += 1
                sudoku_board.pretty_print_board(btracked)
            else:
                print(f"\nbacktracking board {boardChecked} failed\ncontinuing with other boards")
                failed += 1
                
                    
    print(f'''\nTried to find a partial solution amongst {BOARDS_TO_CHECK}
        {failed} failed
        {btSolved} were solved using backtracking
        {boardChecked - btSolved - failed} were solved using AC-3''')

#testBoard(100)
find_partial_solution()