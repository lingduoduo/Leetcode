from typing import List, Optional
###Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        p1 = dummy
        p2 = p1.next

        while p2 and p2.next:
                p3 = p2.next
                p1.next, p3.next, p2.next = p3, p2, p3.next
                p1, p2 = p2, p2.next
        return dummy.next
