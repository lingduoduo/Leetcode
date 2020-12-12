###Definition for singly-linked list.
###class ListNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        curr = l1
        while curr:
            stack1.append(curr)
            curr = curr.next
        
        stack2 = []
        curr = l2
        while curr:
            stack2.append(curr)
            curr = curr.next
        
        dummy = ListNode(-1)
        carry = 0
        curr = dummy
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            par = carry + node1.val + node2.val
            if par >= 10:
                carry = 1
                par = par - 10
            else:
                carry = 0
            node = ListNode(par)
            node.next = dummy.next
            dummy.next = node
        while stack1:
            node1 = stack1.pop()
            par = carry + node1.val
            if par >= 10:
                carry = 1
                par = par - 10
            else:
                carry = 0
            node = ListNode(par)
            node.next = dummy.next
            dummy.next = node
        while stack2:
            node2 = stack2.pop()
            par = carry + node2.val
            if par >= 10:
                carry = 1
                par = par - 10
            else:
                carry = 0
            node = ListNode(par)
            node.next = dummy.next
            dummy.next = node
        if carry == 1:
            node = ListNode(1)
            node.next = dummy.next
            dummy.next = node
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        tmp = 0
        res = ListNode(0)
        while s1 or s2:
            if s1:
                tmp += s1.pop()
            if s2:
                tmp += s2.pop()
            res.val = tmp % 10
            head = ListNode(tmp // 10)
            head.next = res
            res = head
            tmp = tmp // 10
        return res.next if res.val == 0 else res
                
