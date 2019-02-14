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

        curr = dummy.next
        v = dict()
        while curr:
        	try:
        		v[curr.val] += 1
        	except:
        		v[curr.val] = 1
        	curr = curr.next

        curr = dummy
        while curr and curr.next:
        	if v[curr.next.val] == 1:
        		curr = curr.next
        	else:
        		curr.next = curr.next.next
        return dummy.next