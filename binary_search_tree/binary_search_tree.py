"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if self.left is a valid node
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            # First recur on left child 
            self.in_order_print(node.left)
    
            # then print the data of node 
            print(node.value), 
    
            # now recur on right child 
            self.in_order_print(node.right) 
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # Base Case 
        if node is None: 
            return
        
        # Create an empty queue for level order traversal 
        queue = [] 
    
        # Enqueue Root and initialize height 
        queue.append(node)
    
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            print(queue[0].value) 
            current = queue.pop(0) 
    
            #Enqueue left child 
            if current.left is not None: 
                queue.append(current.left) 
    
            # Enqueue right child 
            if current.right is not None: 
                queue.append(current.right) 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node: 
            # First print the data of node 
            print(node.value)
            # Then recur on left child 
            self.dft_print(node.left) 
            # Finally recur on right child 
            self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node: 
    
            # First print the data of node 
            print(node.value), 
    
            # Then recur on left child 
            self.pre_order_dft(node.left) 
    
            # Finally recur on right child 
            self.pre_order_dft(node.right) 

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node: 
    
            # First recur on left child 
            self.post_order_dft(node.left) 
    
            # the recur on right child 
            self.post_order_dft(node.right) 
    
            # now print the data of node 
            print(node.value),
