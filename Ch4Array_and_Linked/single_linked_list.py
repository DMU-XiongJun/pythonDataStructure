class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

    def __str__(self):
        return str(self._data)


class LinkedList:
    def __init__(self, *args):
        self._length = 0  # 单链表的长度
        self._head = None  # 单链表的头结点
        for i in args:
            self.pretend(i)

    def pretend(self, value):
        """在链表的头部插入"""
        self._head = Node(value, self._head)
        self._length += 1
        return value

    def search(self, value):
        """搜索链表中指定项"""
        temp = self._head
        while temp is not None and value != temp._data:
            temp = temp._next
        if temp != None:
            return True
        else:
            return False

    def __getitem__(self, index):
        """搜索索引位置index的项,注意头尾索引的顺序."""
        temp = self._head
        while index > 0:
            temp = temp._next
            index -= 1
        return temp._data

    def __len__(self):
        return self._length

    def replace(self, value, newitem):
        """将单链表中的指定项进行替换，首先应该进行遍历搜索"""
        temp = self._head
        while temp is not None and value != temp._data:
            temp = temp._next
        if temp != None:
            temp._data = newitem
            return True
        else:
            return False

    def replace_by_index(self, index, newitem):
        """在单链表中的指定位置处进行替换"""
        if index < 0 or index >= self._length:
            raise IndexError('替换位置不正确')
        temp = self._head
        while index > 0:
            temp = temp._next
            index -= 1
        temp._data = newitem

    def append(self, item):
        """在单链表末尾插入"""
        if self._head is None:
            self._head = Node(item, self._head)
        else:
            temp = self._head
            newnode = Node(item, None)
            while temp._next is not None:
                temp = temp._next
            temp._next = newnode
        self._length += 1

    def behind_delete(self):
        """从单链表的末尾删除一项"""
        if self._length == 0:
            raise print("the length is less than 1")
        temp = self._head
        if temp._next is None:
            value = self._head._data
            self._head = None
            return value
        while temp._next._next is not None:
            temp = temp._next
        value = temp._next._data
        temp._next = temp._next._next  # 删除末尾处的节点,其中temp._next._next == None
        self._length -= 1
        return value

    def pre_delete(self):
        """从单链表的头部删除"""
        if self._length == 0:
            raise print("The length is less than 1")
        value = self._head._data
        self._head = self._head._next
        self._length -= 1
        return value

    def delete(self, index):
        if index <= 0:
            self.pre_delete()
        elif index >= self._length:
            self.behind_delete()
        else:
            temp = self._head
            while index > 1 and temp._next._next is not None:
                temp = temp._next
                self._length -= 1
            value = temp._next._data
            temp._next = temp._next._next
            self._length -= 1
            return value

    def __str__(self):
        link_ = []
        temp = self._head
        while temp is not None:
            link_.append(temp._data)
            temp = temp._next
        return str(link_)

    def insert(self, index, value):
        """在单链表的指定位置插入一项，首先检验单链表是否为空，然后，检查index是否指向单链表的尾部"""
        if self._length == 0 or index <= 0:
            self.pretend(value)
        elif index >= self._length:
            self.append(value)
        else:
            temp = self._head
            while index > 1:
                temp = temp._next
                index -= 1
            temp._next = Node(value, temp._next)
            self._length += 1
            return value

class LinkedListNil():
    """带哑头节点的循环链表结构"""
    def __init__(self,*args):
        self._length = 0
        self._nil = Node(None,None)
        self._nil._next = self._nil
        for i in args:
            self.append(i)  #注意此处与单链表不同的是，在哑头节点的后面增加节点

    def prepend(self,value):
        """当链表中只有一个哑头节点是，插入第一个节点"""
        temp_node = self._nil
        newnode = Node(value,temp_node._next)
        temp_node._next = newnode
        self._length += 1
        return value

    def append(self,value):
        '''在循环链表中增加节点'''
        temp_node = self._nil
        newnode =Node(value,temp_node)
        while temp_node._next is not self._nil:
            temp_node = temp_node._next
        temp_node._next = newnode
        self._length += 1
        return value

    def insert(self,index,value):
        """在指定位置处插入节点"""
        if self._length == 0 or index <= 0:
            self.prepend(value)
        elif index <= self._length:
            self.append(value)
        else:
            temp_node = self._nil
            while index > 0:
                temp_node = temp_node._next
                index -= 1
            newnode = Node(value,temp_node._next)
            temp_node._next = newnode
            self._length += 1
            return value

    def pre_delete(self):
        """删除链表头部的第一个节点"""
        if self._length == 0:
            raise KeyError("The length is less than 1")
        value = self._nil._next._data
        self._nil._next = self._nil._next._next
        self._length -= 1
        return value

    def behind_delete(self):
        """删除链表的最后一个节点"""
        if self._length == 0:
            raise KeyError("The length is less than 1")
        temp_node = self._nil
        while temp_node._next._next is not self._nil:
            temp_node = temp_node._next
        value = temp_node._next._data
        temp_node._next = temp_node._next._next #此处是遍历到链表的倒数第二个节点
        self._length -= 1
        return value

    def delete(self,index,value):
        """删除链表任意位置处的一个节点"""
        if index <= 0:
            self.pre_delete()
        elif index >= self._length:
            self.behind_delete()
        else:
            temp_node = self._nil
            while index > 0:
                temp_node = temp_node._next
                index -= 1
            value = temp_node._next._data
            temp_node._next = temp_node._next._next #此处同indert操作一样，也是遍历到index之前
            self._length -= 1
            return value

    def search(self, value):
        temp_node = self._nil._next
        while temp_node is not self._nil and value != temp_node._data:
            temp_node = temp_node._next
        if temp_node is self._nil:
            return False
        else:
            return True

    def __len__(self):
        return self._length

    def __str__(self):
        link = []
        temp = self._nil._next
        while temp is not self._nil:
            link.append(temp._data)
            temp = temp._next
        return str(link)










