import nondirectionalgraph


def all_values_alpha_order(root):
    """Returns in alphabetical order all values"""

    data = []

    to_check = [root]

    while to_check:
        node = to_check.pop()

        if node.visted is False:
            data.append(node.data)
            node.visted = True

            for new_neighbor in node.neighbors:
                if new_neighbor.visted is False:
                    to_check.append(new_neighbor)

    data.sort()

    return data


all_values = all_values_alpha_order(nondirectionalgraph.graph_root_1)

nondirectionalgraph.alpha.sort()

#################### Recursively ####################


def all_values_alpha_order_v2(root, values=None):
    """Returns in alphabetical order all values"""

    if values is None:
        values = []

    for node in root.neighbors:
        if node.visted is False:
            node.visted = True
            values.append(node.data)
            all_values_alpha_order_v2(node, values)

    return values


all_values_2 = all_values_alpha_order_v2(nondirectionalgraph.graph_root_2)

nondirectionalgraph.alpha.sort()


# Might not always be True since the graphs are randomly created
# and they might not always connect with the root
if all_values == nondirectionalgraph.alpha:
    print True

if all_values == nondirectionalgraph.alpha:
    print True
