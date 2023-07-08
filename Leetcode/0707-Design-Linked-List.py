class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


class MyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def getNode(self, index):
        n = Node(0, self.head)
        for i in range(index + 1):
            n = n.next
        return n

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        return self.getNode(index).val

    def addAtHead(self, val):
        n = Node(val, self.head)
        self.head = n
        if self.size == 0:
            self.tail = n
        self.size += 1

    def addAtTail(self, val):
        n = Node(val)
        if self.size == 0:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        prev = self.getNode(index - 1)
        n = Node(val, prev.next)
        prev.next = n
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        prev = self.getNode(index - 1)
        prev.next = prev.next.next
        if index == 0:
            self.head = prev.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1


class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


import pysnooper


class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    @pysnooper.snoop()
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        p = self.head
        steps = -1
        while steps < index:
            p = p.next
            steps += 1
        return p.val

    @pysnooper.snoop()
    def addAtHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        self.size += 1

    @pysnooper.snoop()
    def addAtTail(self, val: int) -> None:
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(val)
        self.size += 1

    @pysnooper.snoop()
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        p = self.head
        steps = -1
        while steps < index - 1:
            p = p.next
            steps += 1
        p.next = Node(val, p.next)
        self.size += 1

    @pysnooper.snoop()
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        p = self.head
        steps = -1
        while steps < index - 1:
            p = p.next
            steps += 1
        p.next = p.next.next
        self.size -= 1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy_head.next
        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1


###Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
print(obj.get(0))
obj.addAtTail(3)
print(obj.get(1))
obj.addAtIndex(1, 2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))
