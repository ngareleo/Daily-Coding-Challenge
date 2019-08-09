
"""

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""
""""
Given the root to a binary tree, count the total number of nodes there are.
"""
class Node:

    def __init__(self,val, left = None , right = None):

        self.val = val
        self.left = left
        self.right = right

""" Sample Tree
                2
                ^
        1               3
        ^               ^
    4       x       x       x
"""
def serialize(root):

    String = ""
    if root == None: #check if its an object
        String += "X"
        pass
    elif  (root):

        String += (str(root.val) + ",")
        if (root.left):
            String += (str(root.left.val) + ",")
            serialize(root.left.left)

        if(root.right):
            String += (str(root.right.val) + ",")
            serialize(root.right.right)

    return String

def count(root):

    nodes = 0
    if root:
        nodes += 1

    count(root.left)
    count(root.right)
    return nodes



root_right = Node(3)
root_left_left = Node(4)
root_left = Node(1,root_left_left)
root = Node(2,root_left,root_right)

print(count(root))