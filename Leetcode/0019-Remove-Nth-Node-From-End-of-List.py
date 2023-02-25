#Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        d = dict()
        cnt = 1
        while curr:
           d[cnt] = curr
           cnt+=1
           curr = curr.next

        pos = len(d.keys()) - n

        d[pos].next = d[pos].next.next
        return dummy.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        slow = fast = dummy
        dummy.next = head

        for i in range(n):
            fast = fast.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head






