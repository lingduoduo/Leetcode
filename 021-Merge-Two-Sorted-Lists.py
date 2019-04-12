# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # first try
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            root = ListNode(l1.val)
            l1 = l1.next
            root.next = self.mergeTwoLists(l1, l2)
        else:
            root = ListNode(l2.val)
            l2 = l2.next
            root.next = self.mergeTwoLists(l1, l2)

        return root

        # second try
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next
