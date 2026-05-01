from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0  # (not_rob, rob)

            left_no, left_yes = dfs(node.left)
            right_no, right_yes = dfs(node.right)

            no_rob = max(left_no, left_yes) + max(right_no, right_yes)
            rob = node.val + left_no + right_no

            return no_rob, rob

        return max(dfs(root))


if __name__ == "__main__":
    res = Solution().canSeePersonsCount(heights = [10,6,8,5,11,9])
    print(res)