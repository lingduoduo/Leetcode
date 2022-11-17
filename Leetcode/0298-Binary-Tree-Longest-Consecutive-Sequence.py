# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prev_val, cur_max):
                if not node:
                    return cur_max
                new_max = cur_max + 1 if node.val == prev_val + 1 else 1
                return max(cur_max, dfs(node.left, node.val, new_max), dfs(node.right, node.val, new_max))
        return dfs(root, float('-inf'), 0)