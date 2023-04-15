
class Node(object):
    """a node that can be used for linked list"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """A prettier way of printing our node"""

        return """< Node data: {}  | next: {} >""".format(self.data, self.next)

class Singly_Linked_List(object):
    """A Linked List that only links one way, like a congo line"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        """A prettier way of printing our Linked List"""

        nodes = []
        current = self.head

        while current:
            nodes.append(str(current.data))
            current = current.next

        return "[" + ", ".join(nodes) + "]"

    def append(self, data):
        """Adds node to the end of the linked list"""

        if not self.head:
            self.head = Node(data=data)
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data=data)


def print_Linked_List_Reverse(ll):
    """Prints out the data for the given Linked List in reverse 
    
        >>> ll = Singly_Linked_List()
        >>> ll.append("hello")
        >>> ll.append("world")
        >>> ll.append("you")
        >>> ll.append("amazing!")
        >>> print ll
        [hello, world, you, amazing!]
        >>> print_Linked_List_Reverse(ll)
        amazing!
        you
        world
        hello


    """
    data_in_reversed_order = []

    current = ll.head

    if not current:
        print("")

    else:
        while current.next:
            data_in_reversed_order.insert(0, current.data)
            current = current.next
        data_in_reversed_order.insert(0, current.data)

        for data in data_in_reversed_order:
            print data

ll = Singly_Linked_List()
ll.append("hello")
ll.append("world")
ll.append("you")
ll.append("amazing!")
print ll
print_Linked_List_Reverse(ll)

#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"