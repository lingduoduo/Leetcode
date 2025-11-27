import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked(lists):
    """Convert a list of values into a linked list."""
    dummy = ListNode(0)
    current = dummy
    for value in lists:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store the head of each list with their values and index.
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i, lists[i]))

        dummy = ListNode(-1)
        p = dummy
        while q:
            val, i, node = heapq.heappop(q)
            p.next = ListNode(val)
            p = p.next
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))
        return dummy.next

if __name__ == "__main__":
    numbers = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = [list_to_linked(lst) for lst in numbers]
    result = Solution().mergeKLists(linked_lists)
    current = result
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
