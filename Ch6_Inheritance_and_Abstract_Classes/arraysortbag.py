from Ch4Array_and_Linked.arrays import Arrays
from Ch5_interfaces_inplementations.arraybag import ArrayBag

class ArraySortBag(ArrayBag):
    """An array-based bag implementation"""
    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        ArrayBag.__init__(self,sourceCollection)



    def __contains__(self, item):
        """Returns True if item is in self,or False otherwise.二叉搜索"""
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if self._items[midpoint] == item:
                return True
            elif self._items[midpoint] > item:
                right = midpoint -1
            else:
                left = midpoint + 1
        return False

    def add(self,item):
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self,item)
        else:
            #Resize the array if it is full here
            #Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            for i in range(len(self) , targetIndex , -1):
                self._items[i] = self._items[i-1]
            self._items[targetIndex] = item
            self._size += 1















