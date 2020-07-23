# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if not nums: return None
        #
        # # if len(nums)==1: return TreeNode(nums[0])
        # mid = len(nums) // 2
        # root = TreeNode(nums[mid])
        # left = nums[:mid]
        # right = nums[mid + 1:]
        # if len(left) >= 1:
        #     root.left = self.sortedArrayToBST(left)
        # if len(right) >= 1:
        #     root.right = self.sortedArrayToBST(right)
        # return root
        
        if not nums:
            return None
        
        return self.build(nums, 0, len(nums)-1)
        
    def build(self, arr, left, right):
        if left>right:
            return None
        mid = left + (right - left)//2
        print(mid)
        root = TreeNode(arr[mid])
        root.left = self.build(arr, left, mid-1)
        root.right = self.build(arr, mid+1, right)
        return root
