###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        even = ListNode(0)
        
        oddHead = odd
        evenHead = even
        index = 1
        while head:
            if index % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            index += 1
            head = head.next
        even.next = None
        odd.next = evenHead.next
        return oddHead.next
