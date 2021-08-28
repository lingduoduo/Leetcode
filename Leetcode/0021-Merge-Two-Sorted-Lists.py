###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
           return l2
        if l2 is None:
           return l1
        
        if l1.val < l2.val:
           root = ListNode(l1.val)
           l1 = l1.next
           root.next = self.mergeTwoLists(l1, l2)
        else:
           root = ListNode(l2.val)
           l2 = l2.next
           root.next = self.mergeTwoLists(l1, l2)
        
        return root

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        
        while l1 and l2:
           if l1.val < l2.val:
               curr.next = l1
               l1 = l1.next
               curr = curr.next
           else:
               curr.next = l2
               l2 = l2.next
               curr = curr.next
        
        if l1:
           curr.next = l1
        elif l2:
           curr.next = l2
        
        return dummy.next
        
        if not l1:
            return l2
        if not l2:
            return l1
            
 class Solution(object):
    def mergeTwoLists(self, l1, l2):       
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2 :
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
