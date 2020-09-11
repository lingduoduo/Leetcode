###Definition for singly-linked list.
###class ListNode:
###    def __init__(self, val=0, next=None):
###        self.val = val
###        self.next = next
###Definition for a binary tree node.
###class TreeNode:
###    def __init__(self, val=0, left=None, right=None):
###        self.val = val
###        self.left = left
###        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []

        while head:
        	nums.append(head.val)
        	head = head.next

        return self.helper(nums)

    def helper(self, nums):
        if nums == []:
        	return None

        mid = len(nums)//2

        root = TreeNode(nums[mid])
        root.left = self.helper(nums[:mid])
        root.right = self.helper(nums[mid+1:])

        return root
