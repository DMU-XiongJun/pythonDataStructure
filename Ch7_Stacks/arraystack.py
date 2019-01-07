from Ch4Array_and_Linked.arrays import Arrays
from Ch7_Stacks.abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    DEFAULT_CAPACITY = 10 #For all array stacks
    def __init__(self,sourceCollection = None):
        self._items = Arrays(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self,sourceCollection)

    #Accessors
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]

    def peek(self):
        """Returns the item at top of stack.
        Precondition: the stack is not empty.
        Raise KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._items[len(self) - 1]

    #Mutators
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Arrays(ArrayStack.DEFAULT_CAPACITY)

    def push(self,item):
        """Inserts item at top of stack. Resize array to double here if necessary"""
        if len(self) >= ArrayStack.DEFAULT_CAPACITY:
            temp = Arrays(ArrayStack.DEFAULT_CAPACITY * 2)
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        self._items[len(self)]  =item
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Postcondition: the top item is removed from the stack"""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        #Resize the array here if necessary
        if len(self) < self._items.capacity // 4 and len(self) > ArrayStack.DEFAULT_CAPACITY * 2 :
            temp = Arrays(self._items.capacity // 2)
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        return oldItem




