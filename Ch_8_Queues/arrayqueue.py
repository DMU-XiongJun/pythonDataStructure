from Ch6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractCollection
from Ch4Array_and_Linked.arrays import Arrays

class ArrayQueue(AbstractCollection):
    """array-based queue implementation"""

    DEFAULT_CAPACITY = 10 #for all array queue
    def __init__(self,sourceCollection = None):
        self._items = Arrays(ArrayQueue.DEFAULT_CAPACITY)
        self._front = -1
        self._rear = -1
        AbstractCollection.__init__(self,sourceCollection)

    def add(self,item):
        """Adds item to the rear of the queue."""
        if self.isEmpty():
            self._front = 0
        if len(self) == ArrayQueue.DEFAULT_CAPACITY:     #此时数组满了的话，需要数组的大小
            temp = Arrays(ArrayQueue.DEFAULT_CAPACITY + 1)
            if self._rear > self._front:
                for i in range(len(self)):  #后面所有的len(self)都可以替换成为ArrayQueue.DEFAULT_CAPACITY，以减小运算时间
                    temp[i] = self._items[i]#但用len(self)能更好的帮助理解,循环的终止位置是初始数组的最后一项.
                self._items = temp
            else:
                for i in range(self._front,len(self)):
                    temp[i - self._front] = self._items[i]
                for i in range(self._rear + 1):
                    temp[len(self) - self._front + i] = self._items[i] #此处表示经过上面的for循环之后，
                self._items = temp                   #新数组已经被填满了len(self)-self._front项。
            self._front = 0
            self._rear = len(self) - 1
            ArrayQueue.DEFAULT_CAPACITY += 1
        if self._rear == ArrayQueue.DEFAULT_CAPACITY - 1: #此时rear指针在数组的末尾，故需要在后续的操作中将其重置为0
            self._rear = -1
        self._items[self._rear + 1] = item
        self._rear += 1
        self._size += 1

    def pop(self):
        """Removes and requests the item at top of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty!")
        old_item = self._items[self._front]
        if self._front == ArrayQueue.DEFAULT_CAPACITY - 1:  #此处是front指针指向数组的末尾的情况
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        return old_item

    def __iter__(self):
        """Supports iteration over a view of self."""
        if self._rear > self._front:
            cursor = 0
            while cursor < len(self):
                yield self._items[cursor]
                cursor += 1
        else:
            for i in range(self._front,ArrayQueue.DEFAULT_CAPACITY):
                yield self._items[i]
            for i in range(self._rear + 1):
                yield self._items[i]

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._rear,self._front = -1,-1
        self._items = Arrays(ArrayQueue.DEFAULT_CAPACITY)



