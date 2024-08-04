# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(-1)
        p1 = odd
        even = ListNode(-1)
        p2 = even

        p = head
        cnt = 1
        while p:
            if cnt % 2 == 1:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            cnt += 1
            p = p.next
        p2.next = None
        p1.next = even.next
        return odd.next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        evenhead = even = odd.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head
