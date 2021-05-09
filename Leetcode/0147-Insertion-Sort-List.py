###Definition for singly-linked list.
###class ListNode:
###    def __init__(self, val=0, next=None):
###        self.val = val
###        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        curr = head

        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                temp = curr.next
                curr.next = curr.next.next

                prev = dummy
                while prev.next and prev.next.val <= temp.val:
                    prev = prev.next
                temp.next = prev.next
                prev.next = temp
        return dummy.next               

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        pre = dummy
        node = head
        while node:
            cur = node
            node = node.next
            if cur.val < pre.val:
                pre = dummy
            while pre.next and cur.val > pre.next.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            
        return dummy.next 