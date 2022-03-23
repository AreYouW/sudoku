import random
import sys
from tkinter.tix import Tree
sys.setrecursionlimit(10000)


grid = [[random.randrange(0, 10) for i in range(9)] for j in range(9)]

test_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(grid):
    next_empty = get_empty_value(grid)
    if not next_empty:
        return True
    else:
        row, col = next_empty

    for i in range(1, 10):
        if validate(grid, i, next_empty):
            grid[row][col] = i

            if solve(grid):
                return True

        grid[row][col] = 0

    return False


def validate(grid, number: int, position: tuple):

    for i in range(len(grid[0])):
        if grid[position[0]][i] == number and position[1] != i:
            return False

    for i in range(len(grid)):
        if grid[i][position[1]] == number and position[0] != i:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False

    return True


def print_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j, _val in enumerate(row):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def get_empty_value(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)
    return None


print_grid(test_board)
print(">----------------------------------------------------------<")
solve(test_board)
print_grid(test_board)
