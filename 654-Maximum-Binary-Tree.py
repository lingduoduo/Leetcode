# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
        root.right = self..constructMaximumBinaryTree(nums[idx + 1:])

        return root


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    result = Solution().constructMaximumBinaryTree(nums)
    print(result)
