from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return head

        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy

        p0 = head
        while p0.next:
            if p0.val == p1.val:
                p0 = p0.next
            else:
                p1.next = p0
                p1 = p0
                p0 = p0.next
        p1.next = None
        return dummy.next
