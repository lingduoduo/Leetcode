##Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        self.cut(head, slow)
        # return self.reverse(slow)
        return self.check(head, self.reverse(slow))

    def cut(self, p1, p2):
        while p1.next != p2:
            p1 = p1.next
        p1.next = None

    def reverse(self, p1):
        print(p1.val)
        dummy = ListNode(-1)
        dummy.next = ListNode(p1.val)

        p1 = p1.next
        while p1:
            p2 = p1.next
            p1.next = dummy.next
            dummy.next = p1
            p1 = p2
        return dummy.next

    def check(self, p1, p2):
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, prev.next, slow = slow, None, slow.next
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True


if __name__ == "__main__":
    l = [1, 2, 3, 3, 2, 1]
    # l = [1, 2]
    dummy = ListNode(-1)
    p = dummy
    for v in l:
        p.next = ListNode(v)
        p = p.next

    res = Solution().isPalindrome(dummy.next)
    print(res)

    # p = res
    # vals = []
    # while p:
    #     vals.append(p.val)
    #     p = p.next
    # print(vals)
