###Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            next_one = current.next
            next_two = next_one.next
            next_three = next_two.next

            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one

        return dummy.next


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        while p1.next and p1.next.next:
            p2 = p1.next
            p3 = p2.next

            p2.next = p3.next
            p3.next = p2

            p1.next = p3
            p1 = p2
        return dummy.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy
        while p0.next and p0.next.next:
            p1 = p0.next
            p2 = p1.next

            p0.next, p1.next, p2.next = p2, p2.next, p1
            p0 = p1
        return dummy.next