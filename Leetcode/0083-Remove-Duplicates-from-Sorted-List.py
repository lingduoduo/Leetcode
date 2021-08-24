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
        ###dummy = ListNode(0)
        ###dummy.next = head
        #
        ###curr = dummy
        ###while curr.next and curr.next.next:
        ###    if curr.next.val == curr.next.next.val:
        ###        curr.next = curr.next.next
        ###    else:
        ###        curr = curr.next
        ###return dummy.next
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = q = head
        while p:
            while q and q.val == p.val:
                q = q.next
            p.next = q
            p = q
        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head