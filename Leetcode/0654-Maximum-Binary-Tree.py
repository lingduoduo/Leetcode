from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        idx = i = 0
        max_num = nums[0]

        while i < len(nums):
            if max_num < nums[i]:
                idx = i
                max_num = nums[i]
            i += 1

        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1 :])

        return root


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            p = nums.index(max(nums))
            root = TreeNode(nums[p])
            root.left = self.constructMaximumBinaryTree(nums[:p])
            root.right = self.constructMaximumBinaryTree(nums[p + 1 :])
        return root


if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    result = Solution().constructMaximumBinaryTree(nums)
    print(result)
