# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # if head is None:
        #     return head
        # if k == 0:
        #     return head

        # fast = head
        # n = 0
        # while fast:
        #     fast = fast.next
        #     n += 1
        # k = k % n

        # fast = head
        # while k:
        #     fast = fast.next
        #     k -= 1

        # slow = head
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next

        # fast.next = head
        # head = slow.next
        # slow.next = None
        # return head

        
