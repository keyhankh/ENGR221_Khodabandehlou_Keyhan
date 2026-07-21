""" TODO Your program header """

import turtle

import time 
from memory_profiler import memory_usage

class KochSnowflake:
    def __init__(self, init_length=500, init_depth=3):
        # Initialize the turtle
        self.t = None  

        # Length of one edge at 0 depth
        self.init_length = init_length  
        # Number of "layers" to draw
        self.init_depth = init_depth    
    

    def init_turtle(self):
        """ Initialize the turtle and move it to the 
            appropriate location on the screen """
        

        t = turtle.Turtle() # Initialize the turtle
        t.speed(8) # Increase the turtle's speed

        # Move the turtle to the upper left corner
        t.penup()
        t.goto(-200, -200)
        t.pendown()

        self.t = t


    ######################
    # Draw curve methods #
    ######################

    def draw_curve_recursive(self):
        """ The 'entry point' into the recursive curve method """
        self.draw_curve_recursive_helper(self.init_length, self.init_depth)


    def draw_curve_recursive_helper(self, length, depth):
        """Draw one Koch curve recursively. """

        # Raise an error if depth is negative
        if depth < 0:
            raise ValueError("Depth cannot be negative")

        # Base case
        elif depth == 0:
            self.t.forward(length)

        # Recursive case
        else:
            segment_length = length / 3

            self.draw_curve_recursive_helper(segment_length, depth - 1)

            self.t.left(60)

            self.draw_curve_recursive_helper(segment_length, depth - 1)

            self.t.right(120)

            self.draw_curve_recursive_helper(segment_length, depth - 1)

            self.t.left(60)

            self.draw_curve_recursive_helper(segment_length, depth - 1)
            
    def draw_curve_stack(self):
        """Draw one Koch curve without recursion by using a stack."""

        commands = [("add_curve", self.init_length, self.init_depth)]

        while commands:
            command = commands.pop()

            if command[0] == "add_curve":
                length = command[1]
                depth = command[2]

                if depth < 0:
                    raise ValueError("Depth cannot be negative")

                elif depth == 0:
                    self.t.forward(length)

                else:
                    segment_length = length / 3
                    next_depth = depth - 1

                    commands.append(
                        ("add_curve", segment_length, next_depth)
                    )
                    commands.append(("turn_left",))
                    commands.append(
                        ("add_curve", segment_length, next_depth)
                    )
                    commands.append(("turn_right",))
                    commands.append(
                        ("add_curve", segment_length, next_depth)
                    )
                    commands.append(("turn_left",))
                    commands.append(
                        ("add_curve", segment_length, next_depth)
                    )
            
            elif command[0] == "turn_left":
                self.t.left(60)

            elif command[0] == "turn_right":
                self.t.right(120)

    ##########################
    # Draw snowflake methods #
    ##########################

    def draw_snowflake_recursive(self):
        """ Draw the three edges of the Koch snowflake using the 
            recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_recursive()
            self.t.left(120)
        
        turtle.clearscreen()


    def draw_snowflake_stack(self):
        """ Draw the three edges of the Koch snowflake using the 
            non-recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_stack()
            self.t.left(120)

        turtle.clearscreen()


    #########################@#
    # Compare the approaches! #
    ##########################@

    def compare_snowflake(self):
        """ Compare how much time and memory the recursive and non-recursive 
            implementations of drawing the Koch Snowflake used """
        
        rec_time, rec_mem = self.get_time_and_mem(self.draw_snowflake_recursive)
        nonrec_time, nonrec_mem = self.get_time_and_mem(self.draw_snowflake_stack)

        print(f"Recursive memory usage: {rec_mem} MB")
        print(f"Non-recursive memory usage: {nonrec_mem} MB")
        print()
        print(f"Recursive time taken: {rec_time:.5f} s")
        print(f"Non-recursive time taken: {nonrec_time:.5f} s")
        

    def get_time_and_mem(self, func):
        """ Find the time and memory used by the given function """

        # Start the timer
        time_start = time.perf_counter()
        # Run the function and find the memory used
        mem_usage = memory_usage((func, ), include_children=True, multiprocess=True)
        # End the timer
        time_end = time.perf_counter()

        # Find the total time taken
        time_taken = time_end - time_start 
        # Find the total memory used

        mem_used = max(mem_usage) - min(mem_usage)

        return time_taken, mem_used


if __name__ == "__main__":
    s = KochSnowflake(500, 3)
    s.compare_snowflake()

