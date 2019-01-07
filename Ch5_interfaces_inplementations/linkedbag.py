from Ch4Array_and_Linked.single_linked_list import Node


class LinkedBag(object):
    """A link-based bag implementation."""
    #Constructor
    def __init__(self,sourceCollection = None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        self._items = None
        self._size = None
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

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

    def isEmpty(self):
        """Return True if len(self) == 0,else False."""
        return len(self) == 0

    def __len__(self):
        """Return the number of item in self"""
        return self._size

    def __str__(self):
        """Return the string implementation of self."""
        return "{" + ",".join(map(str, self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        result = LinkedBag(self)  # 创建了self的副本
        for item in other:
            result.add(item)
        return result
    def __eq__(self, other):
        """Return True if self equals other,or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other): return False
        for item in self:
            if not item in other:
                return False
        return True






