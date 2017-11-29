import random


class Node(object):
    """A node that can be used for binary trees"""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """A prettier way of printing our node"""
        if self.left is None:
            left = None
        else:
            left = self.left.data

        if self.right is None:
            right = None
        else:
            right = self.right.data


        return """<Node data: {} | left: {}  right: {}>""".format(
                                self.data,
                                left,
                                right,
                                )


def add_node(root, node):
    """Adds a node to the BST"""

    if node.data < root.data:
        if root.left is None:
            root.left = node
            return
        else:
            add_node(root.left, node)
    if node.data > root.data:
        if root.right is None:
            root.right = node
            return
        else:
            add_node(root.right, node)

    return root


def make_BST(size, nums=None):
    """Makes a random generic BST"""

    if not nums:
        nums = xrange(100)

    mixed_nums = random.sample(nums, size)

    root = Node(mixed_nums.pop())
    while len(mixed_nums) > 0:
        add_node(root, Node(mixed_nums.pop()))

    return root


random_bst = make_BST(10)
