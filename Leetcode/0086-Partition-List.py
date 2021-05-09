###Definition for singly-linked list.
###class ListNode:
###    def __init__(self, x):
###        self.val = x
###        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first = ListNode(0)
        second = ListNode(0)

        dummy1, dummy2 = first, second

        curr = head
        
        while curr:
            if curr.val < x:
                first.next = curr
                first = first.next
            else:
                second.next = curr
                second = second.next
            temp = curr.next
            curr.next = None
            curr = temp
        first.next  = dummy2.next

        return dummy1.next