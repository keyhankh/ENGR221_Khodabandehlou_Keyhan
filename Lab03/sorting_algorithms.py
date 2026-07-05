""" 
Author: Keyhan Khodabandehlou
Last updated: July 5, 2026
Description:
This file contains the SortingAlgorithms class, which creates arrays
and implements selection sort, insertion sort, and bubble sort.
The sorting algorithms use yield statements so the visualizer can
show the sorting process step by step.
"""

import random
import time

from preferences import Preferences

class SortingAlgorithms:
    def __init__(self):
        # The algorithm to sort
        self.array = []

        # Any indices to highlight
        self.inner_idx = -1
        self.outer_idx = -1 

        # A string representing the current sorting algorithm
        self.current_alg = None

        # Store the method of the sorting algorithm being run
        self.alg_method = None
    
    def create_new_array(self, length=Preferences.NUM_ELEMENTS) -> list:
        """ Create a new array to sort """
        return [random.randint(0, Preferences.MAX_VAL) \
                      for _ in range(length)]
    
    def get_next_step(self) -> None:
        """ Updates the value of self.selected_idx whenever we reach 
            a "yield" statement in any of the below sorting algorithms. """
        
        try:
            # Treats the current sorting algorithm as an iterator
            # and sets self.selected_idx to be the next "element"
            self.outer_idx, self.inner_idx = next(self.alg_method)
        # Clear the selected_idx value when we reach the end of the method
        except StopIteration:
            self.outer_idx, self.inner_idx = -1, -1

    def restart(self, new_alg, length=Preferences.NUM_ELEMENTS) -> None:
        """ Restart the sorting process with the new algorithm. 
            Creates a new array to sort. """
        
        self.current_alg = new_alg
        self.alg_method = {
            "selection" : self.selection_sort,
            "insertion" : self.insertion_sort,
            "bubble" : self.bubble_sort
        }[self.current_alg]()
        self.array = self.create_new_array(length)
        self.outer_idx, self.inner_idx = -1, -1

    def selection_sort(self):
        """ An implementation of the Selection sort algorithm. 
            A generator function which creates an iterator that 
            iterates through each "yielded" value. """
        
        # Store length of the array so we know how many items to sort
        n = len(self.array)


        # The outer loop chooses the position we are trying to fill
        # Move through each index in the array; first we find the smallest value for index 0, 
        # then the next smallest value for index 1, and so on
        for i in range(n):

            # Highlight the current outer loop index
            # -1 means ther eis no innder index to highlight yet
            yield -1, i

            # Assume the current index has the smallest value
            # in the unsorted part of the array
            min_idx = i

            # The inner loop checks the rest of the array to see 
            # if there is smaller value than self.array[min_idx]
            for j in range(i + 1, n):


                # Highlight the current smallest value and the value we are comparing it with
                yield min_idx, j

                # If the value at index j is smaller than the current minimum, 
                # update min_idx so it points to the new smallest value
                if self.array[j] < self.array[min_idx]:
                    min_idx = j 
            

            # After checking the rest of the array, min_idx stores the index 
            # of the smallest value in the unsorted section. 
            # Swap that smallest value into the correct position at index i 
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            
            # Highlight the two values that were involved in the swap
            # This lets the visualize show the result of this step
            yield i, min_idx
                

    def insertion_sort(self):
        """ An implementation of the Insertion Sort algorithm.
            This is able to sort the array in-place by moving each value left 
             until it is in the correct position.
            This is a generator function, 
            so it uses yield to show each step in the visualizer.
        """

        # Store the length of the array
        n = len(self.array)

        # Start at index 1 because a list with only the first item can already be considered sorted
        for i in range (1, n):


            # j is the index of the item we are trying to move 
            # into the correct place
            j = i

            # Highlight the current item we are trying to insert
            yield i, j

            # Keep moving the item left while: 
            # 1. j is not at the beginning of the list
            # 2. the item before it is bigger than the current item
            while j > 0 and self.array[j - 1] > self.array[j]:

                # Highlight the two items being compared/swapped
                yield j - 1, j

                # Swap the current item with the item before it
                self.array[j], self.array[j - 1] = self.array[j-1], self.array[j]

                # Move j one position to the left because of the item
                # may still need to move farther left
                j -= 1

                # Highlight the item after it moved
                yield j, j + 1


                
    def bubble_sort(self):
        """ An implementation of the Bubble Sort algorithm.
        This sorts the array in-place by comparing neighboring
        values and swapping them if they are in the wrong order.
        This is a generator function, so it uses yield to show
        each step in the visualizer.
         """

    # Store the length of the array
        n = len(self.array)

    # The outer loop controls how many passes we make through the list
    # After each , one more large value is moved to the end
        for i in range(n - 1):

        # The inner loop compares neighboring values
        # The -i part means we do not re-check values that are already sorted
            for j in range(n - 1 - i):

                # Highlight the two neighboring values being compared
                yield j, j + 1

               # If the left value is bigger than the right value,
               # swap them so the bigger value moves to the right.
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

                    # Highlight the same two values after the swap
                    yield j, j + 1

    def get_runtime(self) -> float:
        """ Returns the length of time (in seconds) that it took for 
            the function_to_run to sort a list of length list_length """

        # Get the time before running
        start_time = time.time()
        # Sort the given list
        for _ in self.alg_method:
            pass
        # Get the time after running
        end_time = time.time()
        # Return the difference
        return end_time - start_time

if __name__ == "__main__":
    s = SortingAlgorithms()
    s.restart("bubble", 10000)
    print(s.get_runtime())