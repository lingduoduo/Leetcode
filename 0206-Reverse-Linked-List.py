# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None:
        #     return None
        #
        # curr1 = head
        # dummy = ListNode(-1)
        # while curr1:
        #     curr2 = curr1.next
        #     curr1.next = dummy.next
        #     dummy.next = curr1
        #     curr1 = curr2
        # return dummy.next
        
        dummy = ListNode(0)

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
        
        
