class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None and pHead.next is None:
            return None

        slow = pHead
        fast = pHead
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        fast = pHead
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return slow
        return None

if __name__ == '__main__':
    root = ListNode(1)
    p = root
    nums = [2, 3, 4, 5, 6]
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    p.next = root.next.next
    res = Solution().EntryNodeOfLoop(root)
    print(res.val)
