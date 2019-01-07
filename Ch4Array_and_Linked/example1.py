class Arrays():
    """Represents an array."""

    def __init__(self, capacity, fillvalue=None):
        self.capacity = capacity
        self._items = list()
        self._logicalSize = 0
        for count in range(capacity):
            if fillvalue is not None:
                self._logicalSize += 1
            self._items.append(fillvalue)

    def __len__(self):
        return self.capacity

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if index < 0 or index >= self._logicalSize:
            raise KeyError("index error")
        return self._items[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self._logicalSize:
            raise KeyError("index error")
        self._items[index] = value

    def grow(self):
        """如果数组的逻辑大小等于其物理大小，将数组的物理大小调整为原来的两倍"""
        temp = Arrays(len(self._items) + 1)
        temp._logicalSize = self._logicalSize
        if self._logicalSize > len(self._items):
            for i in range(self._logicalSize - 1):
                temp[i] = self._items[i]
        else:
            for i in range(self._logicalSize):
                temp[i] = self._items[i]
        self._items = temp

    def shrink(self):
        """如果数组的逻辑大小小于或等于其物理大小的四分之一，并且其物理大小至少是创建数组是默认容量
        的两倍时，减小数组的大小"""
        if self._logicalSize <= len(self._items) // 4 and len(self._items) >= self.capacity * 2:
            temp = Arrays(len(self._items) // 2)
            for i in range(self._logicalSize):
                temp[i] = self._items[i]
            self._items = temp

    def insert(self, index, value):
        """在数组中插入一项,此时要考虑在插入后，数组是否会溢出的问题，如果溢出，则需要增加数组的物理大小"""
        self._logicalSize += 1
        if self._logicalSize > len(self._items):
            self.grow()
        if index >= self._logicalSize - 1:  # 在尾部插入的特殊情况时，不需要移动数组中其他项的位置
            self._items[self._logicalSize - 1] = value
        else:
            for i in range(self._logicalSize - 1, index, -1):
                self._items[i] = self._items[i - 1]
            self._items[index] = value

    def pop(self,index):
        """Precondition:目标位置正确存在"""
        if index < 0 or index >= self._logicalSize:
            raise IndexError
        value = self._items[index]
        for i in range(index,self._logicalSize-1):
            self._items[i] = self._items[i+1]
        self._items[self._logicalSize - 1] = None
        self._logicalSize -= 1
        return value

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        for i in range(self.size()):
            if self.__getitem__(i) != other.__getitem(i):
                return False
        return True

    def size(self):
        return self._logicalSize






