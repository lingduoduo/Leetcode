# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.next if fast else slow