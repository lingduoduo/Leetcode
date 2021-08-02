class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return None

        p1 = head
        while p1 and k > 0:
            p1 = p1.next
            k -= 1

        if k > 0:
            return None

        p2 = head
        while p1:
            p2 = p2.next
            p1 = p1.next
        return p2


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    res = Solution().FindKthToTail(root, 1)
    print(res.val)
