from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(nums):
            if len(nums) == 0: return None

            maxv = max(nums)
            idxm = nums.index(maxv)

            node = TreeNode(maxv)
            node.left = dfs(nums[:idxm])
            node.right = dfs(nums[idxm + 1:])
            return node
        
        return dfs(nums)




        
if __name__ == "__main__":
    res = Solution().canSeePersonsCount(heights = [10,6,8,5,11,9])
    print(res)