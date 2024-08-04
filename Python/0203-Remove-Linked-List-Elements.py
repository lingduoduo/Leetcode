###Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev, curr = dummy, dummy.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next