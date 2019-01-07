from Ch4Array_and_Linked.arrays import Arrays
from Ch6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractCollection
from Ch9_Lists.abstractlist import AbstractList

class ArrayList(AbstractList):
    """An array-based list implementation"""
    DEFAULT_CAPAITY = 10 #for all ArrayList

    def __init__(self,sourceCollection = None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        self._items = Arrays(ArrayList.DEFAULT_CAPAITY)
        AbstractList.__init__(self,sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, i):
        if i < 0 or i > len(self):
            raise IndexError("List index out of range.")
        return self._items[i]

    def __setitem__(self, key, value):
        if key < 0 or key > len(self):
            raise IndexError("List index out of range.")
        self._items[key] = value

    def insert(self,i,item):
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        if i < len(self):
            for j in range(len(self),i,-1):
                self._items[j] = self._items[j - 1]
        self._items[i] = item
        self._size += 1
        self.incModCount()

    def pop(self,i = None):
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")



