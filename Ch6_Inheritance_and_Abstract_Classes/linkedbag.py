from Ch4Array_and_Linked.single_linked_list import Node
from Ch6_Inheritance_and_Abstract_Classes.abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """A link-based bag implementation."""
    #Constructor
    def __init__(self,sourceCollection = None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        self._items = None
        AbstractBag.__init__(self,sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while cursor is not None:
            yield cursor._data
            cursor = cursor._next

    def clear(self):
        """makes self become empty."""
        pass

    def add(self,item):
        """Adds item to self."""
        self._items = Node(item,self._items)
        self._size += 1

    def remove(self,item):
        """Remove item from self.
        Precondition: item is in self.Raises:KeyError if item is not in self.
        Postcondition: item is removed from self"""
        if item not in self:
            raise KeyError(str(item) + "not in bag.")
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe._next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer._next = probe._next
        self._size -= 1







