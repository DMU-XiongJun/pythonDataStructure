from Ch6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractCollection

class AbstractList(AbstractCollection):
    """An abstract list implementation"""

    def __init__(self,sourceCollection):
        """Maintains a count of modifications to the list."""
        self._modCount = 0
        AbstractCollection.__init__(self,sourceCollection)

    def getModCount(self):
        """Returns the count of modifications to the list."""
        return self._modCount

    def incModCount(self):
        self._modCount += 1

    def index(self,item):
        """Precondition :item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + "not in the list.")

    def add(self,item):
        """Adds the item to the end of the list."""
        self.insert(len(self),item)

    def remove(self,item):
        """Removes item from the list.
        Precondition: item is in the list."""
        position = self.index(item)
        self.pop(position)

