###Definition for singly-linked list.
###class ListNode:
###    def __init__(self, val=0, next=None):
###        self.val = val
###        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stack = []
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        return res
