import pygame as interface
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
interface.init()
size = 540
screen = interface.display.set_mode((size, size))
interface.display.set_caption("Sudoku Solver")

# Define fonts
font = interface.font.Font(None, 40)
small_font = interface.font.Font(None, 28)

# Function to draw the Sudoku grid
def draw_grid(grid):
    cell_size = size // 9
    block_size = size // 3

    # Draw background
    screen.fill(WHITE)

    # Draw thicker lines to represent borders between 3x3 subgrids
    for i in range(1, 3):
        interface.draw.line(screen, BLACK, (0, i * block_size), (size, i * block_size), 6)  # Increased line width
        interface.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, size), 6)  # Increased line width

    # Draw thinner lines to outline individual cells
    for i in range(9):
        for j in range(9):
            cell_color = WHITE if (i + j) % 2 == 0 else WHITE
            interface.draw.rect(screen, cell_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            interface.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

            if grid[i][j] != 0:
                if is_safe(grid, i, j, grid[i][j]):
                    text_color = RED  # Set text color to red for the solved cells
                else:
                    text_color = BLACK

                text = font.render(str(grid[i][j]), True, text_color)
                text_rect = text.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

    interface.display.flip()

    cell_size = size // 9
    block_size = size // 3

    # Draw background
    screen.fill(WHITE)

    # Draw thicker lines to represent borders between 3x3 subgrids
    for i in range(1, 3):
        interface.draw.line(screen, BLACK, (0, i * block_size), (size, i * block_size), 6)  # Increased line width
        interface.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, size), 6)  # Increased line width

    # Draw thinner lines to outline individual cells
    for i in range(9):
        for j in range(9):
            cell_color = WHITE if (i + j) % 2 == 0 else WHITE
            interface.draw.rect(screen, cell_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            interface.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 1)

            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

    interface.display.flip()

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j  # Return row, col of empty cell
    return None

def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) \
        and not used_in_col(grid, col, num) \
        and not used_in_box(grid, row - row % 3, col - col % 3, num)

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    for row in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_box(grid, start_row, start_col, num):
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return True
    return False

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # All cells filled, puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True  # If the current number leads to a solution

            grid[row][col] = 0  # Backtrack if current num doesn't lead to solution

    return False  # Trigger backtracking    

# Main loop
running = True
sudoku_solved = False
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


while running:
    screen.fill(WHITE)
    draw_grid(sudoku_grid)
    interface.display.flip()

    for event in interface.event.get():
        if event.type == interface.QUIT:
            running = False

        if event.type == interface.KEYDOWN:
            if event.key == interface.K_SPACE and not sudoku_solved:
                sudoku_solved = solve_sudoku(sudoku_grid)  # Solve the Sudoku puzzle

    # Update the interface if the Sudoku is solved
    if sudoku_solved:
        draw_grid(sudoku_grid)
        interface.display.flip()

interface.quit()
sys.exit()
