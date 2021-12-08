
# Project: Diagonal Sudoku Solver

## Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?
A: *1 search all boxes having two values and find out boxes which have same value in the peers,
    2 according the peers's index, find out boxes which have naked twins number in same rows or same cols and have more than two value
    3 if naked twins number in these cols or rows 's boxes, delete the digit number from these boxese. *

## Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?
A: *1 create two diagoanl units: [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'],
                                  ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']]
    2 apply this units to create peers.
    3 peers['E5'] has 32 peers, other box have 26 peers.(before all box have 20 peers)*

### How to Install

This project requires **Python 3**.

Install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py


