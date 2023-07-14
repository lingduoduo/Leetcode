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


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        node = TreeNode(0)
        # 找到数组中最大的值和对应的下标
        maxValue = 0
        maxValueIndex = 0
        for i in range(len(nums)):
            if nums[i] > maxValue:
                maxValue = nums[i]
                maxValueIndex = i
        node.val = maxValue
        # 最大值所在的下标左区间 构造左子树
        if maxValueIndex > 0:
            new_list = nums[:maxValueIndex]
            node.left = self.constructMaximumBinaryTree(new_list)
        # 最大值所在的下标右区间 构造右子树
        if maxValueIndex < len(nums) - 1:
            new_list = nums[maxValueIndex + 1 :]
            node.right = self.constructMaximumBinaryTree(new_list)
        return node


if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    result = Solution().constructMaximumBinaryTree(nums)
    print(result)
