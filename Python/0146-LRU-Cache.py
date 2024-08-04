import collections


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


class LRUCache:
    def __init__(self, capacity: int):
        self.dic = dict()
        self.capacity = capacity
        self.size = 0
        self.root = ListNode(0, 0)

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if self.size >= self.capacity:
                self.removeFromTail()
                self.size -= 1
            node = ListNode(key, value)
            self.insertIntoHead(node)
            self.dic[key] = node
            self.size += 1

    def removeFromList(self, node):
        if node == self.root:
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None

    def insertIntoHead(self, node):
        head_node = self.root.next
        head_node.prev = node
        node.prev = self.root
        self.root.next = node
        node.next = head_node

    def removeFromTail(self):
        if self.size == 0:
            return
        tail_node = self.root.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            if self.size < self.capacity:
                self.dict[key] = value
                self.size += 1
            else:
                self.dict.popitem(False)
                self.dict[key] = value


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)  # Remove it first before inserting it at the end again
        self.dict[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]
        self.dict[key] = value


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> int:
        if key in self.d:
            old_node = self.d[key]
            self.delete(old_node)

        node = ListNode(key, value)
        self.d[key] = node
        self.add(node)

        if len(self.d) > self.capacity:
            node = self.head.next
            self.delete(node)
            del self.d[node.key]
