# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # first method
        vals = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                vals.append(node.val)
                node = node.next
        vals = sorted(vals)

        dummy = ListNode(-1)
        curr = dummy
        while vals:
            curr.next = ListNode(vals.pop(0))
            curr = curr.next
        return dummy.next
