# 🧩 Sudoku Game

## Overview
Dive into the classic puzzle game with this interactive and engaging Sudoku game, developed in Python using the Pygame library. With a user-friendly interface and a host of features, you'll enjoy solving puzzles of varying difficulty levels.

## Features
- **🌀 Dynamic Grid Generation:** Create a random Sudoku grid based on selected size and difficulty.
- **🧠 Solver:** Utilize a backtracking algorithm to solve any given Sudoku puzzle.
- **💡 Hints:** Get hints for your next move to help progress through the game.
- **🔄 Undo/Redo:** Easily undo or redo moves to refine your strategy.
- **💾 Save/Load:** Save your current game to resume later, or load a previously saved game.

## Getting Started

### Prerequisites
- Python 3.9.9
- Pygame library

### Installation
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/ms2176/sudoku-solver.git
    cd sudoku-solver
    ```
2. Install Pygame if you haven't already:
    ```bash
    pip install pygame
    ```

### How to Play
1. Start the game by running the following command in your terminal:
    ```bash
    python main.py
    ```
2. Use your mouse to select a cell on the grid.
3. Type a number to place it in the selected cell.
4. If you need to clear a cell, use the backspace key.
5. For assistance, press the space key to get a hint.

## Controls
- **🖱️ Mouse:** Select a cell.
- **🔢 Number Keys:** Place a number in the selected cell.
- **⌫ Backspace:** Clear the selected cell.
- **⏎ Return:** Solve the puzzle automatically.
- **🔍 Space:** Get a hint for the next move.
- **↩️ Z:** Undo a move.
- **💾 S:** Save the current game.
- **📂 L:** Load a saved game.

## Technical Details
The game leverages the Pygame library for its graphical user interface and is built around a 2D list structure in Python to represent the Sudoku grid. The puzzle-solving functionality is powered by a backtracking algorithm, ensuring that every puzzle can be solved logically.


## Acknowledgments
- The Sudoku solver algorithm is inspired by the backtracking algorithm.
- The user interface is built using the Pygame library, a cross-platform set of Python modules designed for writing video games.

Enjoy playing Sudoku and challenge yourself with puzzles of varying difficulties! 🧩✨
