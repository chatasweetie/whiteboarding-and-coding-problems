import random


class Node:
    """A node for a graph"""

    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visted = False


    def __repr__(self):
        """A prettier way of printing our node"""

        neighbors = []
        for node in self.neighbors:
            neighbors.append(str(node.data))

        neighbors = ",".join(neighbors)

        return """<Node data: {} | neighbors: [{}]>""".format(
                                self.data,
                                neighbors,
                                )


def create_graph(values):
    """Creates a graph of size"""

    nodes = []
    random.shuffle(values)

    for value in values:
        nodes.append(Node(value))

    for node in nodes:
        num_of_neighbors = random.randint(0, 3)
        while num_of_neighbors:
            neighbor = random.choice(nodes)
            if neighbor is not node and neighbor not in node.neighbors:
                node.neighbors.append(neighbor)
                neighbor.neighbors.append(node)
            num_of_neighbors -= 1

    return nodes[0]


alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

graph_root_1 = create_graph(alpha)

graph_root_2 = create_graph(alpha)
