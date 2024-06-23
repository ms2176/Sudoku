import pygame
import sys
from sudoku_solver import generate_sudoku_grid
from pygame_interface import PygameInterface

def main():
    pygame.init()
    grid = generate_sudoku_grid(9, 0.5)
    size = 9
    difficulty = 0.5
    interface = PygameInterface(grid, size, difficulty)
    interface.run()

if __name__ == "__main__":
    main()