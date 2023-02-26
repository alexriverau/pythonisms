class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for elem in reversed(collection):
                self.insert(elem)

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # for in generator. overwrites dunder __iter__
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    # length generator. overwrites dunder __len__
    def __len__(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter
