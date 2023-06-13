# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        p1 = dummyNode

        for i in range(left - 1):
            p1 = p1.next

        p2 = p1.next
        p4 = None

        for i in range(right - left + 1):
            p3 = p2.next
            p2.next = p4
            p4 = p2
            p2 = p3

        p1.next.next = p2
        p1.next = p4

        return dummyNode.next

