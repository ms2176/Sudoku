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