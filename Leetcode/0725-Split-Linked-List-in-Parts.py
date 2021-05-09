###Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root, k):
        curr = root
        l = 0
        while curr:
            l += 1
            curr = curr.next
        
        parts = [0] * k
        
        if l >= k:
            parts = [l // k] * k
        
        parts[0:l % k] = list(map(lambda x: x + 1, parts[0:l % k]))
        
        ###for i in range(l%k):
        ###    parts[i] += 1
        
        res = []
        curr = root
        for par in parts:
            if par == 0:
                dummy = []
                res.append(dummy)
            else:
                dummy = ListNode(-1)
                curr2 = dummy
                for i in range(par):
                    curr2.next = ListNode(curr.val)
                    curr2 = curr2.next
                    curr = curr.next
                res.append(dummy.next)
        return res


if __name__ == '__main__':
    head = ListNode(1)
    curr = head
    for i in range(2, 4):
        curr.next = ListNode(i)
        curr = curr.next
    
    result = Solution().splitListToParts(head, 5)
    print(result)
