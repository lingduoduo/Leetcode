class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


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
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getNode(self, index: int) -> ListNode:
        if index < 0 or index >= self.size:
            return None
        
        if index < self.size // 2:
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.size - index - 1):
                current = current.prev
        return current

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.getNode(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.size == 0:
            self.head = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            pred = self.getNode(index - 1)
            new_node = ListNode(val, pred, pred.next)
            pred.next.prev = new_node
            pred.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = self.tail = None
        elif index == self.size - 1:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.tail = None
        else:
            node = self.getNode(index)
            node.prev.next = node.next
            node.next.prev = node.prev
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
