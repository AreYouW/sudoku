import random
import sys
import copy as cp
sys.setrecursionlimit(10000)


empty_grid = [[0 for i in range(9)] for j in range(9)]


def make_solvable_grid(num_to_remove):
    cell_positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cell_positions)
    grid = generate_full_valid_grid(empty_grid)
    for i in range(num_to_remove):
        cell = cell_positions[i]
        value = grid[cell[0]][cell[1]]
        grid[cell[0]][cell[1]] = 0
        copy = cp.deepcopy(grid)
        if not solve(copy):
            i += 1
            grid[cell[0]][cell[1]] = value
    return grid


def generate_full_valid_grid(grid):
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(valid_numbers)
    random_cell = get_random_cell()
    if grid[random_cell[0]][random_cell[1]] == 0:
        for x in valid_numbers:
            grid[random_cell[0]][random_cell[1]] = x
            if solve(grid):
                generate_full_valid_grid(grid)

        next_empty = get_empty_value(grid)
        if next_empty:
            grid[random_cell[0]][random_cell[1]] = 0
    return grid


def do_sudoku(grid):
    print_grid(grid)
    print(">----------------------------------------------------------<")
    answer = solve(grid)
    if answer:
        print_grid(grid)
    else:
        print("no valid soln ")


def solve(grid):
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(valid_numbers)
    next_empty = get_empty_value(grid)
    if not next_empty:
        return True

    for i in valid_numbers:
        if validate_square(grid, i, next_empty):
            grid[next_empty[0]][next_empty[1]] = i

            if solve(grid):
                return True

        grid[next_empty[0]][next_empty[1]] = 0

    return False


def validate_square(grid, number: int, position: tuple):

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


def get_random_cell():
    return (random.randrange(1, 9), random.randrange(1, 9))


do_sudoku(make_solvable_grid(48))