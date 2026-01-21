from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = q = head
        while p:
            while q and q.val == p.val:
                q = q.next
            p.next = q
            p = q
        return head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
                continue
            p = p.next
        return head