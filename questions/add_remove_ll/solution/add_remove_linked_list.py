class Node(object):
    """A node that can be used for data structures"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """A prettier way of printing our node"""

        return """<Node data: {} next: {} >""".format(
                                self.data,
                                self.next,
                                )


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

        return '[' + ', '.join(nodes) + ']'

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


ll = Singly_Linked_List()
ll.append("hello")
ll.append("world")
ll.append(True)
ll.append("True")
print ll
ll.remove(True)
print ll
ll.remove("hello")
print ll
