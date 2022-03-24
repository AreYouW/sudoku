import random
import sys
sys.setrecursionlimit(10000)


grid = [[random.randrange(0, 10) for i in range(9)] for j in range(9)]

test_invalid_grid = [
    [0,0,4,0,6,0,0,0,5],
    [7,8,0,4,0,0,0,2,0],
    [0,0,2,6,0,1,0,7,8],
    [6,1,0,0,7,5,0,0,9],
    [0,0,7,5,4,0,0,6,1],
    [0,0,1,7,5,0,9,3,0],
    [0,7,0,3,0,0,0,1,0],
    [0,4,0,2,0,6,0,0,7],
    [0,2,0,0,0,7,4,0,0],
]

test_valid_grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

empty_grid = [[0 for i in range(9)] for j in range(9)]

def generate_grid(grid):
    valid_numbers = [1,2,3,4,5,6,7,8,9]
    random_cell = (random.randrange(1, 9),random.randrange(1, 9))
    random.shuffle(valid_numbers)
    if grid[random_cell[0]][random_cell[1]] == 0:
        for x in valid_numbers:
            grid[random_cell[0]][random_cell[1]] = x
            if solve(grid):
                generate_grid(grid)
                
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
    valid_numbers = [1,2,3,4,5,6,7,8,9]
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

a = generate_grid(empty_grid)
print_grid(a)
# do_sudoku(test_valid_grid)
# do_sudoku(test_invalid_grid)
# do_sudoku(grid)