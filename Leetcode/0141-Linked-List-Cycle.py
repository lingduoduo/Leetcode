###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ###visited = set()
        ###while head is not None:
        ###	if head in visited:
        ###		return True
        ###	visited.add(head)
        ###	head = head.next
        ###return False
        ###slow = fast = head
        ###if fast is None:
        ###    return False
        ###while fast is not None:
        ###    if fast.next is None:
        ###        return False
        ###    fast = fast.next.next
        ###    slow = slow.next
        ###    if fast == slow:
        ###        return True
        ###return False
        
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.nest
            slow = slow.next
            if fast == slow:
                return True
        return False
