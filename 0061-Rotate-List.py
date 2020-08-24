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

        curr = head
        n = 0
        while curr:
            n+=1
            curr = curr.next

        if n<2:
            return head

        k=k%n
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
        




