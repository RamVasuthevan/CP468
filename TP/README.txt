To run this program, you must have python 3.7 or higher installed. https://www.python.org/downloads/

Next, install matplotlib using pip. https://pip.pypa.io/en/stable/quickstart/

Then, you can run either dejong_test.py, himmelblau_test.py, or rosenbrock_test.py to see the test's reults display. 
This calls the SGA funtion in simple_genetic_algorithm.py and performs mating, reproduction and mutation operations 
on as many generations of a population of specified sizes. The program will plot each generation's fittest member's fitness measure. 
This graph can be saved as a .png file.

#Note
It is possible to compare 2 different bit mutation methods by alternating the commented out sections in the attempt_mutation() function.