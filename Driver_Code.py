# This program is the driver code and the user interface.
# All backend processes except getting input from the user,
# are encapsulated and abstracted.
from Processes import processWrapper

import sys


#Driver Code
if __name__ == '__main__':
    """
    Variables:
    n = Number of nodes in the Binary tree.
    A = An array storing n integers (values of the nodes of the Binary tree).
    target = The data node to be deleted. 
            0 for root node, 
            1 for left child at level 1 Left Node, 
            2 for level 2 right node, so on.
    """
    # Get the number of nodes in the tree.
    n = int(input("No of elements: "))

    # Store the space separated integers as a Python list.
    A = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

    # Get the target node to be processed.
    target = int(input("Enter target node: "))

    # If the target node entred is more than or equal to the number of nodes entered,
    # The process can not be completed. 
    # Because node numbering is between the range(0, n-1). 
    # Therefore, exit the program execution.
    if target >= n:
        sys.exit("Node deletion not possible. Target node exceeds the permissible limit.")

    else:
        # else, proceed with the execution.
        processWrapper(A, target)

        

        




