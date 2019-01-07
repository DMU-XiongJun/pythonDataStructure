from Ch4Array_and_Linked.arrays import Arrays
from Ch6_Inheritance_and_Abstract_Classes.abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation"""
    # class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self,which includes the contents of sourceCollection,
        if it's present."""
        self._items = Arrays(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self,sourceCollection)

    def clear(self):
        """makes self become empty."""
        self._size = 0
        self._items = Arrays(ArrayBag.DEFAULT_CAPACITY)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def add(self, item):
        """Adds item to self."""
        if len(self) >= self._items.capacity:
            temp = Arrays(self._items.capacity * 2)
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        self._items[len(self)] = item  # 应该尽可能地在self上调用方法或函数以完成一些事情。例如当需要使用包的逻辑大小时，
        self._size += 1  # 运行len(self)，而不是直接使用self._size。

    def __getitem__(self, item):
        return self._items[item]

    def remove(self, item):
        """Remove item from self.
        Precondition: item is in self.Raises:KeyError if item is not in self.
        Postcondition: item is removed from self"""
        if item not in self:
            raise KeyError(str(item) + 'not in bag')
        #搜索底层数组以查找目标项的位置
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        #将数组中的项向左移动，以填补删除项所留下来的“空缺”，并将包的大小减1.
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i+1]
        self._size -= 1
        if len(self) <= self._items.capacity // 4 and len(self) > ArrayBag.DEFAULT_CAPACITY * 2 :
            temp = Arrays(self._items.capacity / 2)
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp




if __name__ == '__main__':
    c = ArrayBag([1, 2, 3, 4, 5, 6])
    b = [7, 8, 9, 10, 11, 33, 3, 3, 3, 3, 3, 3, 23, 23, 23, 23, 2, 32, 3, 2, 32, 3, 12, 321, 3, 213, 21, 32, 13, 123, 123,
         12312, 3, 21, 12, 312, 3, 123, 1, 23,123,12,312,3,12,312,3,123,12,3,12,31,23,12,312,312,31,23,1,23,]
    print(len(b))
    d = c.__add__(b)
    print(d)
    print(len(d))
    print(d._items.capacity)
    for i in range(59):
        d.remove(d[4])
    print(len(d))
    print(d._items.capacity) #此处有一未解决的将数组容量减小的bug调试，


