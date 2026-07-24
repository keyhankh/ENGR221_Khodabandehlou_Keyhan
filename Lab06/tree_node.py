""" 
Author: Keyhan Khodabandehlou
Last updated: July 24, 2026 """

from enum import Enum


class TreeNode:
    def __init__(self, name, node_type, data=None):
        self.name = name # Used to identify and display this node
        self.node_type = node_type # Describes whether node is school, program, or faculty node
        self.data = data # stores  extra info
        self.parent = None # parent is none until this node is added as a child
        self.children = [] # a general tree node can have any number of children


    def add_child(self, child) -> None:
        """Adds a child to this node and updates the child's parent."""

        # Add the new child to this node's list of children
        self.children.append(child)

        # Connect the child back to its parent
        child.parent = self



    def remove_child(self, child) -> None:
        """ Removes a child from this node if the child is present. """

        # Only remove the child if it belongs in this node
        if child in self.children:
            self.children.remove(child)

            # The removed node no longer has a parent - disconnect child from this tree
            child.parent = None




    def is_leaf(self) -> bool:
        """Returns True when this node has no children."""

        # A leaf node has an empty children list - node at the bottom of the tree
        return len(self.children) == 0



    def depth(self) -> int:
        """Returns the number of edges from this node to the root."""

        # start at the current node with a depth of zero
        node_depth = 0
        current_node = self

        # Move upward through each parent until reaching root 
        while current_node.parent is not None: 
            node_depth += 1
            current_node = current_node.parent
        
        return node_depth
    



    def height(self) -> int:
        """Returns the number of edges in the longest path to a leaf"""

        # Base case: A leaf has no edges below, so height = 0
        if self.is_leaf():
            return 0
        
        child_heights = []

        # recursively calculates the height of every child subtree
        for child in self.children: 
            child_heights.append(child.height())

        # Use the tallest child subtree and include the connecting edge 
        return 1 + max(child_heights)




    def find(self, name):
        """Returns the node with the given name, or None if not found."""

        # Checks whether the current node is the requested node before searching below it
        if self.name == name: 
            return self
        
        # Recursively search thru each child's subtree
        for child in self.children: 
            found_node = child.find(name)

            # Stop searching as soon as a matching node is found
            if found_node is not None: 
                return found_node
            
        # The name was not found anywhere below this node 
        return None
    



    def print_tree(self, indent=0):
        """ Prints the tree with indentation. """
        # Indent the node based on its level in the tree
        print("    " * indent + str(self))

        # Recursively print every child one level deeper
        for child in self.children:
            child.print_tree(indent + 1)


    def __str__(self):
        """Returns the name of this tree node."""
        return self.name
    

    class NodeType(Enum):
        # These values identify role of each node in the faculty tree
        SCHOOL = "School"
        PROGRAM = "Program"

        #  kept since the provided tests use the misspelled name
        PROGAM = "Program"

        FACULTY = "Faculty"

        @classmethod
        def init_from_str(cls, node_type):
            return cls[node_type.strip().upper()]

if __name__ == "__main__":
     # It creates a small example tree for testing and demonstration.

    # Create the root node
    root = TreeNode("Engineering", TreeNode.NodeType.SCHOOL)


    # Create two program nodes and attach them to the root
    comp_e = TreeNode("CompE", TreeNode.NodeType.PROGAM)
    root.add_child(comp_e)

    ee = TreeNode("EE", TreeNode.NodeType.PROGAM)
    root.add_child(ee)

    # Create faculty leaf nodes under the CompE program
    kubota = TreeNode("Kubota", TreeNode.NodeType.FACULTY)
    comp_e.add_child(kubota)

    qin = TreeNode("Qin", TreeNode.NodeType.FACULTY)
    comp_e.add_child(qin)


    # Display the finished tree structure
    root.print_tree()