# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

        

