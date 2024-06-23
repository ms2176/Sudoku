import pygame as interface
import sys

class Config:
    size = 540
    colors = {
        "WHITE": (255, 255, 255),
        "BLACK": (0, 0, 0),
        "GREEN": (0, 255, 0),
        "RED": (255, 0, 0)
    }
    fonts = {}

interface.init()
interface.font.init()

Config.fonts = {
    "main": interface.font.Font(None, 40),
    "small": interface.font.Font(None, 28)
}

def draw_grid(screen, grid):
    try:
        cell_size = Config.size // 9
        block_size = Config.size // 3
        screen.fill(Config.colors["WHITE"])

        def draw_lines_and_cells():
            for i in range(1, 3):
                interface.draw.line(screen, Config.colors["BLACK"], (0, i * block_size), (Config.size, i * block_size), 6)
                interface.draw.line(screen, Config.colors["BLACK"], (i * block_size, 0), (i * block_size, Config.size), 6)
            for i in range(9):
                for j in range(9):
                    cell_color = Config.colors["WHITE"]
                    interface.draw.rect(screen, cell_color, (j * cell_size, i * cell_size, cell_size, cell_size))
                    interface.draw.rect(screen, Config.colors["BLACK"], (j * cell_size, i * cell_size, cell_size, cell_size), 1)
                    if grid[i][j] != 0:
                        text_color = Config.colors["RED"] if not is_safe(grid, i, j, grid[i][j]) else Config.colors["BLACK"]
                        text = Config.fonts["main"].render(str(grid[i][j]), True, text_color)
                        text_rect = text.get_rect(center=(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2))
                        screen.blit(text, text_rect)

        draw_lines_and_cells()
        interface.display.flip()
    except Exception as e:
        print(f"Error drawing grid: {e}")

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0], l[1] = row, col
                return True
    return False

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    return num in [grid[i][col] for i in range(9)]

def used_in_box(grid, box_start_row, box_start_col, num):
    return any(num in grid[i][box_start_col:box_start_col+3] for i in range(box_start_row, box_start_row+3))

def is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row - row % 3, col - col % 3, num)

def solve_sudoku(grid):
    l = [0, 0]
    if not find_empty_location(grid, l):
        return True
    row, col = l[0], l[1]

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def main():
    screen = interface.display.set_mode((Config.size, Config.size))
    clock = interface.time.Clock()
    selected = None
    running = True

    # Initialize the grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Add a status message
    status_message = ""

    while running:
        for event in interface.event.get():
            if event.type == interface.QUIT:
                running = False
            elif event.type == interface.MOUSEBUTTONDOWN:
                pos = interface.mouse.get_pos()
                selected = get_cell_from_pos(pos)
                status_message = ""
            elif event.type == interface.KEYDOWN:
                if selected:
                    row, col = selected
                    if event.unicode.isdigit() and event.unicode != '0':
                        num = int(event.unicode)
                        if is_safe(grid, row, col, num):
                            grid[row][col] = num
                            status_message = f"Placed {num} at ({row+1}, {col+1})"
                        else:
                            status_message = f"Cannot place {num} at ({row+1}, {col+1})"
                    elif event.key == interface.K_BACKSPACE:
                        grid[row][col] = 0
                        status_message = f"Cleared cell at ({row+1}, {col+1})"
                    elif event.key == interface.K_RETURN:
                        if solve_sudoku(grid):
                            status_message = "Puzzle solved!"
                        else:
                            status_message = "No solution exists for this puzzle."
                elif event.key == interface.K_r:
                    grid = [[0 for _ in range(9)] for _ in range(9)]
                    status_message = "Grid reset"

        screen.fill(Config.colors["WHITE"])
        draw_grid(screen, grid)
        if selected:
            highlight_cell(screen, selected)

        # Display status message
        status_text = Config.fonts["small"].render(status_message, True, Config.colors["BLACK"])
        screen.blit(status_text, (10, Config.size - 30))

        interface.display.flip()
        clock.tick(30)    
        screen = interface.display.set_mode((Config.size, Config.size))
    clock = interface.time.Clock()
    selected = None
    running = True

    # Initialize the grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    while running:
        for event in interface.event.get():
            if event.type == interface.QUIT:
                running = False
            elif event.type == interface.MOUSEBUTTONDOWN:
                pos = interface.mouse.get_pos()
                selected = get_cell_from_pos(pos)
            elif event.type == interface.KEYDOWN:
                if selected and event.unicode.isdigit():
                    row, col = selected
                    num = int(event.unicode)
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        selected = None

                if event.key == interface.K_SPACE:
                    solve_sudoku(grid)
                elif event.key == interface.K_BACKSPACE:
                    if selected:
                        grid[selected[0]][selected[1]] = 0
                        selected = None

        screen.fill(Config.colors["WHITE"])
        draw_grid(screen, grid)
        if selected:
            highlight_cell(screen, selected)

        interface.display.flip()
        clock.tick(30)

def get_cell_from_pos(pos):
    x, y = pos
    cell_size = Config.size // 9
    row, col = y // cell_size, x // cell_size
    if row < 9 and col < 9:
        return (row, col)
    return None

def highlight_cell(screen, position):
    cell_size = Config.size // 9
    row, col = position
    interface.draw.rect(screen, Config.colors["GREEN"], (col * cell_size, row * cell_size, cell_size, cell_size), 3)

if __name__ == "__main__":
    main()
    interface.quit()
    sys.exit()