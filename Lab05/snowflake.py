""" 
Author: Keyhan Khodabandehlou
Last updated: July 2026
Description: 
Draws a Koch snowflake using both recursion and an explicit stack. 
The program also compares the runtime and memory usage of the two approaches.
 """

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
        t.speed(0) # # Use a faster animation speed so deeper snowflakes finish sooner

        t.pencolor('#ff0000') # temporary to find fix
        t.pensize(4)

        # Move the turtle to the lower-left area so the snowflake is centered
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

        # Recursive case: replace one line with four smaller Koch curves
    def draw_curve_recursive_helper(self, length, depth):
        """Draw one Koch curve recursively. """

        # A negative depth is invalid because recursion must eventually reach 0
        if depth < 0:
            raise ValueError("Depth cannot be negative")

        # Base case: at depth 0, draw one straight line segment
        elif depth == 0:
            self.t.forward(length)

        # Recursive case: replace one line with four smaller Koch curves
        else:
            # each smaller curve is one-third the length of the current curve. 
            segment_length = length / 3

            # Draw the first smaller section
            self.draw_curve_recursive_helper(segment_length, depth - 1)

            # Turn outward to begin  traingular bump 
            self.t.left(60)

            # draw second smaller section
            self.draw_curve_recursive_helper(segment_length, depth - 1)

            # turn in the opposite direction across the center of the bump
            self.t.right(120)


            # Draw the third smaller section
            self.draw_curve_recursive_helper(segment_length, depth - 1)

            # Return to the original direction
            self.t.left(60)

            
            # Draw the fourth and final smaller section
            self.draw_curve_recursive_helper(segment_length, depth - 1)
            
    def draw_curve_stack(self):
        """Draw one Koch curve without recursion by using a stack."""

        # Begin with one command representing entire side of the snowflake. 
        commands = [("add_curve", self.init_length, self.init_depth)]

        # continue until every drawing and turnign command has been completed
        while commands:
            # pop() removes the most recently added command, following Last in, First OUt (LIFO) order 
            command = commands.pop()

            if command[0] == "add_curve":
                # extract the length and epth stored in the command tuple
                length = command[1]
                depth = command[2]

                if depth < 0:
                    raise ValueError("Depth cannot be negative")

                # Base case: draw a straight segment
                elif depth == 0:
                    self.t.forward(length)

                else:
                    # Break the current curve into four smaller curves
                    segment_length = length / 3
                    next_depth = depth - 1

                    # Commands are added in reverse order since a stack is LIFO.
                    #  Last comand appended will be the first command processed
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
            
            # Execute a stored left-turn command
            elif command[0] == "turn_left":
                self.t.left(60)

            # execute a stored right-turn command
            elif command[0] == "turn_right":
                self.t.right(120)

    ##########################
    # Draw snowflake methods #
    ##########################

    def draw_snowflake_recursive(self): # Draw 3 koch curves, turning 120 degrees after each side
        """ Draw the three edges of the Koch snowflake using the 
            recursive curve method """

        self.init_turtle()

        # a Koch snowflake has three Koch-curve sides
        for _ in range(3):
            self.draw_curve_recursive()
            # turn 120 degrees to begin the next side of the triangle
            self.t.left(120)

        # reset the turtle window so another version can be measured. 
        turtle.done()


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
        
        # measure the recursive implmenetation first
        rec_time, rec_mem = self.get_time_and_mem(self.draw_snowflake_recursive)

        # measure the explicit-stack implementation second
        nonrec_time, nonrec_mem = self.get_time_and_mem(self.draw_snowflake_stack)

        print(f"Recursive memory usage: {rec_mem} MB")
        print(f"Non-recursive memory usage: {nonrec_mem} MB")
        print()
        print(f"Recursive time taken: {rec_time:.5f} s")
        print(f"Non-recursive time taken: {nonrec_time:.5f} s")
        

    # save the time immediately before the function runs
    def get_time_and_mem(self, func):
        """ Find the time and memory used by the given function """

        # Start the timer
        time_start = time.perf_counter()
        # Run the function and find the memory used
        mem_usage = memory_usage((func, ), include_children=True, multiprocess=True)
        # Save the time immediately after the function finishes
        time_end = time.perf_counter()

        # Runtime is the difference between the ending and starting times
        time_taken = time_end - time_start 



        # Estimate additional memory used by finding the difference
        # between the highest and lowest recorded memory samples
        mem_used = max(mem_usage) - min(mem_usage)

        return time_taken, mem_used


if __name__ == "__main__":
    s = KochSnowflake(500, 1)
    s.draw_snowflake_recursive()

