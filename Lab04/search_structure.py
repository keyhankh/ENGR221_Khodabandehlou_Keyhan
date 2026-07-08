""" TODO
Author: Keyhan Khodabandehlou!
Last Updated: July 8, 2026
search_structure.py defines custome Queue and Stack classes used for BFS and DFS search!
"""

class Queue():
    def __init__(self):
        # Creates an empty list to store the queue items
        self.items = []

    def add(self, item) -> None:
        """ "Enqueue" the item to the end of the queue """
        # Queue = FIFO. New Items go to back/end of list
        self.items.append(item)

    def remove(self):
        """ Dequeue" the item from the queue and return it """
        # Remove oldest item, which is at index 0 
        return self.items.pop(0)
    
    def is_empty(self) -> bool:
        """ Returns whether or not the queue is empty """
        # If list length is 0, the queue is empty
        return len(self.items) == 0
        
    

class Stack():
    def __init__(self):
        # Create an empty list to store the stack items
        self.items = []

    def add(self, item) -> None:
        """ Push an item to the top of the stack """
        # Stack = LIFO. Top of stack is the end of the list
        self.items.append(item)

    def remove(self):
        """ Pop an item from the stack and return it """
        # Remove newest item, which is at end of the list
        return self.items.pop()
    
    def is_empty(self) -> bool:
        """ Returns whether or not the stack is empty """
        # If list length is 0, the stack is empty
        return len(self.items) == 0