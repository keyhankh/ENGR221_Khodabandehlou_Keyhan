# ENGR221_Khodabandehlou_Keyhan

Name: Keyhan Khodabandehlou
Course: ENGR 221
Semester: Summer 2026

# Lab 3: Sorting Algorithms

## Description

This lab implements a pygame sorting visualizer. The program creates an array of carrots with different lengths and shows how sorting algorithms organize carrots from smallest to largest. Sorting algorithms used in this lab include selection sort, insertion sort, and bubble sort
## Files

- `controller.py`: Controls the main logic of the program, including keyboard input, restarting the array, selecting the sorting algorithm, and updating each sorting step.

- `display.py`: Handles the graphics. It draws the carrot array, highlighted indices, carrot values, and visual changes on the screen.

- `preferences.py`: Stores constant values used throughout the program, such as the number of elements, maximum carrot value, screen size, colors, timing, and image paths.

- `sorting_algorithms.py`: Stores the array and contains the sorting algorithms. This is the main file I modified for the lab.

- `images/`: Stores the image files used to draw the carrots and highlighted markers.

- `answers.txt`: Contains my written answers for the homework questions.


## Sorting Algorithms Implemented

The following algorithms are included:

- Selection Sort
- Insertion Sort
- Bubble Sort

Each algorithm sorts the array in-place and uses `yield` so the program can show each step visually.


## How to Run

From the `Lab03` folder, run:

```bash
python3 controller.py