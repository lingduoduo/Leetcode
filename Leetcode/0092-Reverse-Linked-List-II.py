# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        q = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return q

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        p1 = dummy
        p2 = p1.next
        p3 = p2.next
        p2.next = None

        p2 = p3
        while p2:
            p3 = p2.next
            p2.next = p1.next
            p1.next = p2
            p2 = p3
        return dummy.next
