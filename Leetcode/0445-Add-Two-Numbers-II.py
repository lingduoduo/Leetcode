###Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None


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

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1Stack = []
        p = l1
        while p:
            l1Stack.append(p.val)
            p = p.next

        l2Stack = []
        p = l2
        while p:
            l2Stack.append(p.val)
            p = p.next

        head = ListNode(-1)
        p = head
        carry = 0
        while l1Stack or l2Stack or carry:
            x = l1Stack.pop() if l1Stack else 0
            y = l2Stack.pop() if l2Stack else 0
            v = x + y + carry
            newnode = ListNode(v % 10)
            newnode.next = p.next
            p.next = newnode
            carry = v // 10
        return head.next


if __name__ == "__main__":
    l = [7, 2, 4, 3]
    head1 = ListNode(-1)
    cur = head1
    for i in range(len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next

    l = [5, 6, 4]
    head2 = ListNode(-1)
    cur = head2
    for i in range(len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next

    res = Solution().addTwoNumbers(head1.next, head2.next)
    p = res
    while p:
        print(p.val)
        p = p.next
