class Node:
    """A node that can be used for data structures"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """A prettier way of printing our node"""
        if self.next is None:
            next_data = None
        else:
            next_data = self.next.data

        return """<Node | data: {} | next: {} >""".format(
                                self.data,
                                next_data,
                                )


class Singly_Linked_List:
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

        return '[' + ', '.join(nodes) + ']'

    def adds_at_index(self, index, data):
        """Adds node to a particular index in a linked list"""

        current = self.head

        to_add_node = Node(data=data)

        if index == 0:
            if current is not None:
                to_add_node.next = current

            self.head = to_add_node
            return

        while index - 1:
            print current
            current = current.next

        to_add_node.next = current.next
        current.next = to_add_node

    def append(self, data):
        """Adds node to the end of the linked list"""

        if not self.head:
            self.head = Node(data=data)
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data=data)

    def remove(self, data):
        """Removes the first occurence of data in the linked list"""

        current = self.head
        previous = None

        if current.data == data:
            if current.next:
                self.head = current.next
            else:
                self.head = None

            return

        while current.next and current.data != data:
            previous = current
            current = current.next

        if current.data == data:
            previous.next = current.next
            current.next = None

    def removes_at_index(self, index):
        """Removes node at index in the linked list"""

        current = self.head
        previous = None

        if index == 0:
            if current is not None:
                previous = current.next
            self.head = previous

        while current.next:

            previous = current
            current = current.next

            index -= 1

            if index == 0:
                previous.next = current.next
                break



