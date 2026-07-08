# ENGR221_Khodabandehlou_Keyhan


Name: Keyhan Khodabandehlou
Course: ENGR 221
Semester: Summer 2026

# Lab 3: Sorting Algorithms

## Description

This lab implements movement and search algorithms for a duck-collecting game. 
The player moves around the board collecting duck food, and each collected duck becomes part of the player's body. 
The lab also implements Stack and Queue data structures, which are used for DFS and BFS search in AI mode.

## Files

- `controller.py`: Runs the game and handles keyboard input.


- `game_data.py` - Stores the board, player/body, food, movement logic, and AI search logic

- `cell.py` - Defines each cell on the board and whether it is empty, food, player, or body

- `search_structure.py` - Defines the custom Stack and Queue classes used for DFS and BFS

- `preferences.py` - Stores constants such as board size, colors, images, and timing

- `display.py` - Draws the game board, score, player, body, food, and game-over screen

- `answers.txt` - Contains written answers for the lab questions

- `tests/` - Contains tests for the Stack and Queue classes


## AI Search Implemented

The lab includes AI movement that searches for food automatically.

- BFS uses a Queue and usually finds the shortest path to food.

- DFS uses a Stack and may find food, but it does not guarantee the shortest path.




## How to Run Tests

From the `Lab04` folder, run:

```bash
python3 -m pytest -v -m stack tests/structures_tests.py


## How to Run 

python3 controller.py


## To turn on AI mode while the game is running, press:

a