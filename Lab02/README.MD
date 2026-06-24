# Lab 2: Antarctic Survival

## Description

This lab implements a pygame game called Antarctic Survival. The player controls a penguin that moves around the board, eats fish, and avoids enemy seals.

## Files

- `controller.py`: Controls the game loop, keyboard input, food updates, enemy updates, and screen refreshes.

- `boardDisplay.py`: Handles drawing the board, player, food, enemies, score, and game over message.

- `cell.py`: Defines the Cell class and the possible cell types: player, empty, food, and enemy.

- `gameData.py`: Stores and updates the game state, including the board, player position, food, enemies, score, and game over status. This is the main file I modified.

- `preferences.py`: Stores constant values used throughout the game, such as board size, colors, image paths, timing, and game over text.

- `images/`: Stores the image files for the penguin, fish, and seal.

- `part1.txt`: Contains answers to the Part 1 questions.

- `pseudocode2_2.txt`: Contains pseudocode for player movement.

- `pseudocode2_3.txt`: Contains pseudocode for adding and eating food.

- `pseudocode2_4.txt`: Contains pseudocode for enemy mechanics.

## How to Run

From the Lab02 folder, run:

```bash
python3 controller.py

## Customization

For my game customization, I changed the game over message in `preferences.py`.

Original message:

```text
You were eaten by a seal!
Press any key to exit.

