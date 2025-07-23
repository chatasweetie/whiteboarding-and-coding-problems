class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove(self, value):
        if self.head is None:
            return  # List is empty, nothing to delete

        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.value != value:
            current_node = current_node.next

        if current_node.next:  # We found the value
            current_node.next = current_node.next.next

    def __repr__(self):
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return " -> ".join(nodes) + " -> None"

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
print(ll)  # Output: 1 -> 2 -> 3 -> None

ll.prepend(0)
print(ll)  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.remove(2)
print(ll)  # Output: 0 -> 1 -> 3 -> None
