# Definition for singly-linked list with a random pointer.
class Node:
    def init(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodedict = dict()
        dummy = Node(0, None, None)
        nodedict[head] = dummy
        
        newCurr, curr = dummy, head
        while curr:
            node = Node(curr.val, curr.next, None)
            nodedict[curr] = node
            newCurr.next = node
            newCurr = newCurr.next
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                nodedict[curr].random = nodedict[curr.random]
            curr = curr.next
        return dummy.next
