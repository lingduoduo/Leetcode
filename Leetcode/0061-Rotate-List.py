class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        if n < 2:
            return head

        k = k % n
        if k == 0:
            return head

        p1, p2 = head, head
        for i in range(k):
            p2 = p2.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next

        output = p1.next
        p1.next = None
        p2.next = head

        return output


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        n = 0
        p = dummy
        while p.next:
            p = p.next
            n += 1

        if n < 2:
            return dummy.next

        k = k % n

        f, s = dummy.next, dummy.next
        for i in range(k):
            f = f.next

        while f.next:
            s = s.next
            f = f.next

        f.next = dummy.next
        dummy.next = s.next
        s.next = None

        return dummy.next
