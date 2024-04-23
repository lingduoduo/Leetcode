import collections
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.buildTree(preorder[1: 1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

        


if __name__ == "__main__":
    res = Solution().productExceptSelf(nums = [-1,1,0,-3,3])
    print(res)  

