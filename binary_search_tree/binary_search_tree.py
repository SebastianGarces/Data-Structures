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

"""
    The left subtree of a node contains only nodes with values lesser than the node’s value.
    The right subtree of a node contains only nodes with values greater than the node’s value.
    The left and right subtree each must also be a binary search tree.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"v: {self.value}, l: {self.left}, r: {self.right}"

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new node value is less than the current node value
        # if there is no left child already here
        # add new node to the left
        # create a BST Node and encapsulate the value in it
        # then set it to the left
        # otherwise call insert on the left node
        # check if the new node value is more than the current node value
        # if there is no right child already here
        # add new node to the right
        # create a BST Node and encapsulate the value in it
        # then set it to the right
        # otherwise call insert on the right node
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)
        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target matches the current node value
        # return True
        # check if the target is less than the current node value
        # if there is not left child already here
        # return False
        # otherwise
        # return a call of contains on the left child passing in the target value
        # check if the target is more than the current node value
        # if there is not right child already here
        # return False
        # otherwise
        # return a call of contains on the right child passing in the target value

        if target == self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # recursive approach:
        # check if there is no node to the right
        # return node value
        # otherwise
        # return a call of get_max on right node

        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def get_min(self):
        # recursive approach:
        # check if there is no node to the left
        # return node value
        # otherwise
        # return a call of get_max on left node

        if not self.left:
            return self.value
        else:
            return self.left.get_min()

        # ------------------------------------------------- #

        # interative approach:
        # current_node = self.value
        # max_value = 0
        # while current_node is not None:
        # if current_node.value > max_value:
        # max_value = current_node.value
        # current_node = current_node.right
        # return max_value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call the function passing the current node's value
        # if there is something to the left
        # call the function on the left value

        # if there is a node to the right
        # call the function on the right node
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
