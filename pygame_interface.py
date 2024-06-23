import pygame
import sys
from sudoku_solver import solve_sudoku, is_safe, get_hint, generate_sudoku_grid

class PygameInterface:
    def __init__(self, grid, size, difficulty):
        self.grid = grid
        self.size = size
        self.difficulty = difficulty
        self.screen = pygame.display.set_mode((size * 50, size * 50 + 50))
        pygame.display.set_caption("Sudoku")
        self.clock = pygame.time.Clock()
        self.selected = None
        self.status_message = ""
        self.font = pygame.font.Font(None, 32)
        self.colors = {
            "background": (255, 255, 255),
            "grid": (0, 0, 0),
            "selected": (255, 0, 0),
            "text": (0, 0, 0)
        }
        self.history = []

    def draw_grid(self):
        for i in range(self.size + 1):
            thickness = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, self.colors["grid"], (i * 50, 0), (i * 50, self.size * 50), thickness)
            pygame.draw.line(self.screen, self.colors["grid"], (0, i * 50), (self.size * 50, i * 50), thickness)

    def draw_numbers(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]!= 0:
                    text = self.font.render(str(self.grid[i][j]), True, self.colors["text"])
                    self.screen.blit(text, (j * 50 + 20, i * 50 + 15))

    def highlight_cell(self):
        if self.selected:
            row, col = self.selected
            pygame.draw.rect(self.screen, self.colors["selected"], (col * 50, row * 50, 50, 50), 2)

    def display_status(self):
        text = self.font.render(self.status_message, True, self.colors["text"])
        self.screen.blit(text, (10, self.size * 50 + 10))

    def get_cell_from_pos(self, pos):
        x, y = pos
        if x < 0 or x > self.size * 50 or y < 0 or y > self.size * 50:
            return None
        return y // 50, x // 50

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.selected = self.get_cell_from_pos(pos)
                    self.status_message = ""
                elif event.type == pygame.KEYDOWN:
                    if self.selected:
                        row, col = self.selected
                        if event.unicode.isdigit() and event.unicode!= '0':
                            num = int(event.unicode)
                            if is_safe(self.grid, row, col, num):
                                self.grid[row][col] = num
                                self.history.append((row, col, num))
                                self.status_message = f"Placed {num} at ({row+1}, {col+1})"
                            else:
                                self.status_message = f"Cannot place {num} at ({row+1}, {col+1})"
                        elif event.key == pygame.K_BACKSPACE:
                           self.grid[row][col] = 0
                           self.history.append((row, col, 0))
                           self.status_message = f"Cleared cell at ({row+1}, {col+1})"
                        elif event.key == pygame.K_RETURN:
                            if solve_sudoku(self.grid):
                                self.status_message = "Puzzle solved!"
                            else:
                                self.status_message = "No solution exists for this puzzle."
                    elif event.key == pygame.K_r:
                        self.grid = generate_sudoku_grid(self.size, self.difficulty)
                        self.history = []
                        self.status_message = "Grid reset"
                    elif event.key == pygame.K_SPACE:
                        hint = get_hint(self.grid)
                        if hint:
                            row, col, num = hint
                            self.grid[row][col] = num
                            self.history.append((row, col, num))
                            self.status_message = f"Hint: Placed {num} at ({row+1}, {col+1})"
                        else:
                            self.status_message = "No hint available"
                    elif event.key == pygame.K_z:
                        if self.history:
                            row, col, num = self.history.pop()
                            self.grid[row][col] = 0
                            self.status_message = f"Undo: Cleared cell at ({row+1}, {col+1})"
                        else:
                            self.status_message = "No undo available"
                    elif event.key == pygame.K_s:
                        with open("save.txt", "w") as f:
                            for row in self.grid:
                                f.write(" ".join(str(cell) for cell in row) + "\n")
                        self.status_message = "Game saved"
                    elif event.key == pygame.K_l:
                        try:
                            with open("save.txt", "r") as f:
                                self.grid = [[int(cell) for cell in row.split()] for row in f.readlines()]
                            self.history = []
                            self.status_message = "Game loaded"
                        except FileNotFoundError:
                            self.status_message = "No saved game found"

            self.screen.fill(self.colors["background"])
            self.draw_grid()
            self.draw_numbers()
            self.highlight_cell()
            self.display_status()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()