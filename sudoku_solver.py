import random

def is_safe(grid, row, col, num):
    """
    Check if it will be legal to assign num to the given row, col
    """
    for x in range(len(grid)):
        if grid[row][x] == num:
            return False

    for x in range(len(grid)):
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    """
    Solve the Sudoku puzzle using backtracking
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                for num in range(1, len(grid) + 1):
                    if is_safe(grid, i, j, num):
                        grid[i][j] = num
                        if solve_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def generate_sudoku_grid(size=9, difficulty=0.5):
    """
    Generate a random Sudoku grid with a given size and difficulty
    """
    grid = [[0]*size for _ in range(size)]
    def generate_grid(row=0, col=0):
        if row == size - 1 and col == size:
            return True
        if col == size:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return generate_grid(row, col + 1)
        for num in random.sample(range(1, size + 1), size):
            if is_safe(grid, row, col, num):
                grid[row][col] = num
                if generate_grid(row, col + 1):
                    return True
        grid[row][col] = 0
        return False
    generate_grid()
    # Remove some numbers to make it solvable
    for i in range(size):
        for j in range(size):
            if random.random() < difficulty:
                grid[i][j] = 0
    return grid

def get_hint(grid):
    """
    Get a hint for the next move
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                for num in range(1, len(grid) + 1):
                    if is_safe(grid, i, j, num):
                        return i, j, num
    return None