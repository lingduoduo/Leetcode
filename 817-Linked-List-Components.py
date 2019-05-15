'''
Input: 
head: 0->1->2->3
G = [0, 1, 3]
'''

import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        d = collections.Counter(G)
        res = 0
        curr = head
        while curr:
            if curr.val in d and (not curr.next or curr.next.val not in d)
                res += 1
            curr = curr.next
        return res


if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    G = [0, 1, 3]
    result = Solution().numComponents(head, G)
    print(result)
    
    head.next.next.next.next = ListNode(4)
    G = [0, 3, 1, 4]
    result = Solution().numComponents(head, G)
    print(result)
