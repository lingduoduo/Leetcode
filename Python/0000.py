from typing import List
import heapq
from collections import defaultdict

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
        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node
    
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
            self.cach[key] = node
            self._add_to_tail(node)
        else:
            node = ListNode(key, value)
            node.val = value
            self._move_to_tail(node)
        
        if self.capacity > len(self.cache):
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    res = Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    print(res)
