import math
import time
import numpy as np

from print_grid import print_board


def possible_number(i, j, grid, n):                                         # Checks whether number n can go at location i,j
    grid[j, i] = 0                                                          # Temporarily replaces the tested square to 0 so does not count as having the number in the row or column
    for x in range(9):
        if grid[j, x] == n or grid[x, i] == n:
            grid[j, i] = n
            return 0
    square_nos = []
    for h in range(3):
        for g in range(3):
            square_nos.append(grid[math.floor(j / 3) * 3 + h, math.floor(i / 3) * 3 + g])
    if n in square_nos:
        grid[j, i] = n
        return 0
    grid[j, i] = n
    return 1


def get_coordinates(grid):
    numbers_to_solve = []
    for i in range(9):
        for j in range(9):
            if grid[i, j] == 0:
                numbers_to_solve.append((j, i))
    return numbers_to_solve                                                 # List of tuples with the coordinates of all the squares that need to be solved


def sudoku_solver(grid):
    coords = get_coordinates(grid)
    print_board(grid)
    num_to_solve = len(coords)
    k = 0
    iter = 0
    while k < num_to_solve:
        if grid[coords[k][1], coords[k][0]] < 9:
            grid[coords[k][1], coords[k][0]] += 1
            point = grid[coords[k][1], coords[k][0]]
            num = possible_number(coords[k][0], coords[k][1], grid, point)
            if num == 1:  # Carries on if it is a plausible number
                k += 1
            elif num == 0:
                if grid[coords[k][1], coords[k][0]] == 9:                   # If number does not work and has already reached 9, so need to reset and iterate back to the last square
                    grid[coords[k][1], coords[k][0]] = 0
                    k -= 1
        else:
            grid[coords[k][1], coords[k][0]] = 0                            # Need to manage for the case where goes back to the previous square which is already a 9
            k -= 1
        iter += 1
        if iter % 1600 == 0:
            print_board(grid)
            print("Number of iterations: {}".format(iter))
    print("\n\n")
    print_board(grid)
    print("Number of iterations: {}".format(iter))


grid_input = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]])

start_time = time.time()
sudoku_solver(grid_input)
print("The Sudoku has been solved in {} seconds".format(time.time() - start_time))
