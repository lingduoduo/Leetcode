###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        current=dummy

        while current.next and current.next.next:
            next_one=current.next
            next_two=next_one.next
            next_three=next_two.next

            current.next=next_two
            next_two.next=next_one
            next_one.next=next_three
            current=next_one

        return dummy.next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while pre.next and pre.next.next:
            cur, pos = pre.next, pre.next.next
            cur.next = pos.next
            pos.next = cur
            pre.next = pos
            pre = cur
        return dummy.next

