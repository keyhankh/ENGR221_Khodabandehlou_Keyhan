"""
Author: Keyhan Khodabandehlou
Last updated: July 24, 2026
Description:
Imports engineering faculty information from an Excel file, stores the
professors in a dictionary, builds a faculty tree, and displays the tree.
"""

import pandas as pd

from professor import Professor
from faculty_visualizer import FacultyVisualizer
from tree_node import TreeNode
from preferences import Preferences

class ENGR_Faculty:
    def __init__(self):
        
        # Dictionary containing the faculty nodes
        # Keys are last names, values are Professors
        self.faculty_dict = self.import_faculty()

        # Tree representing the Engineering faculty
        self.program_structure = self.build_structure()

        # Visualize the faculty tree
        self.visualizer = FacultyVisualizer(
            self.program_structure, self.faculty_dict)

        
    def import_faculty(self):
        """ Reads the Excel file containing the faculty member information
            and adds them to the faculty dictionary """
        
        # The dictionary to store the faculty
        faculty_dict = {}

        # Read the Excel file into a pandas data frame
        df = pd.read_excel(Preferences.FACULTY_FILE)


        # Add each row of the data frame (professor) to the dictionary
        df.apply((lambda x: self.add_prof(x, faculty_dict)), axis=1)

        return faculty_dict


    def add_prof(self, prof, faculty_dict) -> None:
        """Creates a Professor object and adds it to the faculty dictionary."""

        # Create a Professor using the info from one DataFrame row
        professor = Professor(
            prof["FirstName"], 
            prof["LastName"],
            prof["Rank"],
            prof["Program"],
            prof["Office"],
        )

        # Store the professor using the last name as the dictionary key
        faculty_dict[professor.last_name] = professor

    def build_structure(self) -> TreeNode:
        """Builds and returns the School of Engineering faculty tree."""
        # We are all under the School of Engineering

        # Creating the root of the tree
        root = TreeNode(
            "School of Engineering", 
            TreeNode.NodeType.SCHOOL
        )
        
        # Create a node for each SoE program
        for program in Professor.Program:
            program_node = TreeNode(
                program.value,
                TreeNode.NodeType.PROGRAM
            )

            root.add_child(program_node)

            # Add each professor under the appropriate program. 
            for professor in self.faculty_dict.values():
                if professor.program == program:
                    faculty_node = TreeNode (
                        professor.last_name,
                        TreeNode.NodeType.FACULTY,
                        professor
                    )

                    program_node.add_child(faculty_node)

        return root


    def visualize_faculty(self):
        """ Build and show the tree visualizing the faculty """
        self.visualizer.run()
        

if __name__ == '__main__':
    f = ENGR_Faculty()
    f.visualize_faculty()