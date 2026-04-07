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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        prv, nxt = None, s
        while nxt:
            nxt.next, prv, nxt = prv, nxt, nxt.next
        
        p1 = head
        p2 = prv
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
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
