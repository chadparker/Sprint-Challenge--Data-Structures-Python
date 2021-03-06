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

# from queue import Queue
# from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if (self.left is None) and (self.right is None):
            return self.value
        
        # recursive approach:
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # iterative approach:
        # current = self
        # max_val = self.value
        # while current:
        #     if current.value > max_val:
        #         max_val = current.value
        #     current = current.right
        # return max_val

        # awesome iterative approach:
        while self.right:
            self = self.right
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
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self): # use a queue
        # queue = Queue()
        # queue.enqueue(self)

        # while len(queue) > 0:
        #     current_node = queue.dequeue()
            
        #     print(current_node.value)

        #     if current_node.left:
        #         queue.enqueue(current_node.left)
            
        #     if current_node.right:
        #         queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self): # use a stack
        # stack = Stack()
        # stack.push(self)

        # while len(stack) > 0:
        #     current_node = stack.pop()

        #     print(current_node.value)

        #     if current_node.left:
        #         stack.push(current_node.left)
            
        #     if current_node.right:
        #         stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):

        print(self.value)
        
        if self.left:
            self.left.pre_order_dft()

        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):

        if self.left:
            self.left.post_order_dft()

        if self.right:
            self.right.post_order_dft()

        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  
