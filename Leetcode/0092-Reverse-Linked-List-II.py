from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        p1 = dummyNode

        for i in range(left - 1):
            p1 = p1.next

        cur = p1.next
        pre = None

        for i in range(right - left + 1):
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        p1.next.next = cur
        p1.next = pre

        return dummyNode.next
