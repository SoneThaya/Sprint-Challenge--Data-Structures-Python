class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # sets 1's prev to be None
        self.prev = None
        # store 1 in a variable
        # 1 will be current
        current = self.head
        
        
        while current is not None:
            # first loop
            # store current's next in a variable before chaning pointers
            # next will be 1's next which is 2
            next = current.next_node
            # 1's next will be prev which is None
            current.next_node = prev
            # 1 will be current
            prev = current
            # current will be 2 from earlier
            current = next
            # repeat until next_node is None
        # make last node the head
        self.head = prev
