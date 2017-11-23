# Use this morce code tree to access the root node
# note that the root node has no value


class Tree(object):
    """The Tree"""

    def __init__(self):
        self.root = None


class Node(object):
    """A node that can be used for data structures"""

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

morse_code_tree = Tree()
morse_code_tree.root = Node("")
morse_code_tree.root.left = Node("e")
morse_code_tree.root.right = Node("t")

morse_code_tree.root.left.left = Node("i")
morse_code_tree.root.left.right = Node("a")
morse_code_tree.root.right.left = Node("n")
morse_code_tree.root.right.right = Node("m")

morse_code_tree.root.left.left.left = Node("s")
morse_code_tree.root.left.left.right = Node("u")
morse_code_tree.root.left.right.left = Node("r")
morse_code_tree.root.left.right.right = Node("w")
morse_code_tree.root.right.left.left = Node("d")
morse_code_tree.root.right.left.right = Node("k")
morse_code_tree.root.right.right.left = Node("g")
morse_code_tree.root.right.right.right = Node("o")

morse_code_tree.root.left.left.left.left = Node("h")
morse_code_tree.root.left.left.left.right = Node("v")
morse_code_tree.root.left.left.right.left = Node("f")
morse_code_tree.root.left.right.left.left = Node("l")
morse_code_tree.root.left.right.right.left = Node("p")
morse_code_tree.root.left.right.right.right = Node("j")
morse_code_tree.root.right.left.left.left = Node("b")
morse_code_tree.root.right.left.left.right = Node("x")
morse_code_tree.root.right.left.right.left = Node("c")
morse_code_tree.root.right.left.right.right = Node("y")
morse_code_tree.root.right.right.left.left = Node("z")
morse_code_tree.root.right.right.left.right = Node("q")
