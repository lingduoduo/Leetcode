###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy.next
        v = dict()
        while curr:
            try:
                v[curr.val] += 1
            except:
                v[curr.val] = 1
            curr = curr.next

        curr = dummy
        while curr and curr.next:
            if v[curr.next.val] == 1:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = collections.defaultdict()
        curr = head
        while curr:
            if curr.val in d:
                d[curr.val] += 1
            else:
                d[curr.val] = 1
            curr = curr.next

        dummy = ListNode(-1)
        curr = dummy
        for k, v in d.items():
            if v == 1:
                curr.next = ListNode(k)
                curr = curr.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head


        curr, prev = head, dummy
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return dummy.next 

