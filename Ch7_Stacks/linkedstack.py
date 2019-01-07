from Ch4Array_and_Linked.single_linked_list import Node
from Ch7_Stacks.abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    def __init__(self,sourceCollection = None):
        """Link-based stack implementation"""
        self._items = None
        AbstractStack.__init__(self,sourceCollection)

    #Accessors
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        def visitNodes(node):
            if not node is None:
                tempList.append(node._data)
                visitNodes(node._next)
        tempList = list()
        visitNodes(self._items)
        return iter(tempList)

    def peek(self):
        """Returns the item at top of stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise KeyError('the stack is empty!')
        return self._items._data

    #Mutators
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def push(self,item):
        """Inserts item at top of stack."""
        self._items = Node(item,self._items)
        self._size += 1

    def pop(self):
        """Remove and returns the item at top of stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise KeyError("the stack is Empty!")
        oldItem = self._items._data
        self._items = self._items._next
        self._size -= 1
        return oldItem





