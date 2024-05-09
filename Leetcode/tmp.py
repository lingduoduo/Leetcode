from typing import List, Optional
import heapq
from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def child(self,node,bottom,nexx):
        curr=bottom
        while curr.next:
            if curr.child:
                self.child(curr,curr.child,curr.next)
            curr=curr.next
        node.next=bottom
        bottom.prev=node
        node.child=None
        curr.next=nexx
        if nexx:
            nexx.prev=curr
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        p = head
        while p:
            if p.child:
                nexx = p.next
                self.child(p, p.child, nexx)
            temp=temp.next
        return head

    
# Test the code        
if __name__ == '__main__':
    res = Solution().twoCitySchedCost(costs = [[10,20],[30,200],[400,50],[30,20]])
    print(res)
