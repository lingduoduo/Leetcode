###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ###first try
        ###stack1 = list()
        ###stack2 = list()
        #
        ###curr = headA
        ###while curr:
        ###    stack1.append(curr)
        ###    curr = curr.next
        ###curr = headB
        ###while curr:
        ###    stack2.append(curr)
        ###    curr = curr.next
        #
        ###result = None
        ###while stack1 and stack2:
        ###    s1 = stack1.pop()
        ###    s2 = stack2.pop()
        ###    if s1 != s2:
        ###        return result
        ###    else:
        ###        result = s1
        ###return result
        
        ###second try
        p1 = headA
        p2 = headB
        
        while p1!=p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
                
        return p1
