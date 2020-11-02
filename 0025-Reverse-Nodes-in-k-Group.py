# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #实现一个group内的变换
        def reverse(head, k):
            #判断长度是否小于k，小于则不反转
            p = head
            for i in range(k):
                if p:
                    p = p.next
                else:
                    return head

            pre, cur = head, head.next
            pre.next = None
            i = 1
            while cur and i < k:
                nex = cur.next
                cur.next = pre
                pre, cur = cur, nex
                i += 1

            if cur:
                head.next = reverse(cur, k)

            return pre

        if(head):
            return reverse(head, k)
        else:
            return None