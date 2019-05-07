# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
