To run this program, you must have python 3.7 or higher installed. https://www.python.org/downloads/

Next, install matplotlib and numpy using pip. https://pip.pypa.io/en/stable/quickstart/

Then, you can run test.py. By default it will run on the the 98th, 99th, 100th, and 101st boards in sudoku_small.csv. The first two boards can/will be solved with AC3, while the last two boards can/will be solved with backtracking. The program will create a graph of the queue lengths at each step in the AC3 algorithm, for each sudoku it solves. This graph is saved in the queue_length.png file.

Input is taken from sudoku_small.csv. The format of that file is that the first line contains "quizzes,solutions\n" while all of the following lines contain two comma separated lists of numbers. The numbers represent the board, with zeros representing empty spaces. The board is arranged by filling in the rows from left to right and then top to bottom with the numbers. 