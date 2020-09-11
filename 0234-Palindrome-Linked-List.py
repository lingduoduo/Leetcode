###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ###l = list()
        ###while head:
        ###    l.append(head.val)
        ###    head = head.next
        ###if l == l[::-1]:
        ###    return True
        ###else:
        ###    return False
        
        
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