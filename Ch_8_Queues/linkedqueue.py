from Ch6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractCollection
from Ch4Array_and_Linked.single_linked_list import Node


class LinkQueue(AbstractCollection):
    """Link-based queue implementation."""

    def __init__(self, sourceCollection=None):
        self._front = None
        self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, item):
        """Adds item to the rear of the queue."""
        new_node = Node(item, None)
        if self.isEmpty():
            self._front = new_node
        else:
            self._rear._next = new_node
        self._rear = new_node
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError('the queue is empty!')
        old_item = self._front._data
        self._front = self._front._next
        if self._front is None:
            self._rear = None  # 此时回到初始空队列状态
        self._size -= 1
        return old_item

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from top to bottom of queue."""

        def visitNode(node):
            if node is not None:
                temp_list.append(node._data)
                visitNode(node._next)

        temp_list = list()
        visitNode(self._front)
        return iter(temp_list)

    def clear(self):
        self._size = 0
        self._front, self._rear = None, None

