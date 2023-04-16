
class Stack(object):
    """a simple stack: last in, first out"""

    def __init__(self):
        self.__stack = []

    def peek(self):
        """returns the next out item"""
        if self.__stack:
            return self.__stack[-1]
        else:
            print "nothing here"
            return

    def pop(self):
        """returns the next item"""
        return self.__stack.pop()

    def push(self, data):
        """adds an item to the stack"""
        self.__stack.append(data)

    def is_empty(self):
        """returns bool if stack is empty"""
        return not bool(self.__stack)


class Queue(object):
    """A Queue class that uses two stacks under the hood

        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> q.enqueue(4)
        >>> q.enqueue(5)
        >>> q.dequeue()
        >>> q.last()
        5
        >>> q.first()
        2
        >>> q.is_empty()
        False

        >>> b = Queue()
        >>> b.is_empty()
        True

    """

    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()

    def enqueue(self, data):
        """adds an item to the Queue"""
        self.__stack1.push(data)

    def __move_items_over(self):
        """moves all the items from stack 1 to stack 2"""
        while not self.__stack1.is_empty():
            self.__stack2.push(self.__stack1.pop())

    def __move_items_back(self):
        """moves all the items from stack 2 to stack 1"""
        while not self.__stack2.is_empty():
            self.__stack1.push(self.__stack2.pop())

    def dequeue(self):
        """removes an item from the queue"""

        self.__move_items_over()

        self.__stack2.pop()

        self.__move_items_back()

    def first(self):
        """similar to peek, for the next item"""
        self.__move_items_over()

        print self.__stack2.peek()

        self.__move_items_back()

    def last(self):
        """similar to peek, for the last item"""

        print self.__stack1.peek()

    def is_empty(self):
        """returns bool if stack is empty"""

        return self.__stack1.is_empty()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()

#####################################################################
# Don't touch the code below!
# This allows the doctests to run

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"