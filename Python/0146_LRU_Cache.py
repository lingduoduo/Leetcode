import collections


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

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # remove least recently used


class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_tail(self, node: ListNode):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node

        self.tail.prev = node
        node.next = self.tail
    
    def _move_to_tail(self, node: ListNode):
        self._remove(node)
        self._add_to_tail(node)
    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value)
            self.cache[key] = node
            self._add_to_tail(node)
        else:
            node = self.cache[key]
            node.val = value
            self._move_to_tail(node)
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


