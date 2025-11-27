from typing import List, Optional
###Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy
        while p0.next and p0.next.next:
            p1 = p0.next
            p2 = p1.next

            # swap
            p0.next = p2
            p1.next = p2.next
            p2.next = p1

            # move p0 forward
            p0 = p1

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy
        while p0.next and p0.next.next:
            p1 = p0.next
            p2 = p1.next

            p0.next, p1.next, p2.next = p2, p2.next, p1
            p0 = p1
        return dummy.next