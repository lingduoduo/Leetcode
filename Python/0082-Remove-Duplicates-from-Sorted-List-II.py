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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        post = head.next

        while post:
            while post and post.val != cur.val:  # 没有重复的时候
                post = post.next
                cur = cur.next
                pre = pre.next
            while post and post.val == cur.val:  # 有重复的时候
                post = post.next
            if post != cur.next:  # 只有在有重复的时候这么做
                pre.next = post
                cur = post
                if post is not None:
                    post = post.next

        return dummy.next
