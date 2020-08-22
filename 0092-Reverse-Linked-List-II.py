# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and count < m:
            pre = pre.next
            count += 1
        if count < m:
            return head
        mNode = pre.next
        curr = mNode.next
        while curr and count < n:
            out = curr.next
            curr.next = pre.next
            pre.next = curr
            mNode.next = out
            curr = out
            count += 1
        return dummy.next
