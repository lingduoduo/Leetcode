from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return None

        max_sum, res, level = float('-inf'), 0, 0
        q = [root]
        while q:
            level += 1
            tot = 0
            for _ in range(len(q)):
                node = q.pop(0)
                tot += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < tot:
                max_sum, res = tot, level
        return res

if __name__ == "__main__":
    Solution().maxLevelSum()


