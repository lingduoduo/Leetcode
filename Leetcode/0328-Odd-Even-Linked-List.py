###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None

# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         odd = ListNode(0)
#         even = ListNode(0)
#
#         oddHead = odd
#         evenHead = even
#         index = 1
#         while head:
#             if index % 2 == 1:
#                 odd.next = head
#                 odd = odd.next
#             else:
#                 even.next = head
#                 even = even.next
#             index += 1
#             head = head.next
#         even.next = None
#         odd.next = evenHead.next
#         return oddHead.next

# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = ListNode(-1)
        pt_odd = odd
        even = ListNode(-1)
        pt_even = even

        p = head
        cnt = 1
        while p:
            if cnt % 2 == 1:
                pt_odd.next = p
                pt_odd = pt_odd.next
            else:
                pt_even.next = p
                pt_even = pt_even.next
            p = p.next
            cnt += 1
        pt_even.next = None
        pt_odd.next = even.next
        return odd.next

