from  collections import Counter
from typing import List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_bts(root):
            if not root:
                return []
            return inorder_bts(root.left) + [root] + inorder_bts(root.right)

        def construct_bst(left, right, path):
            if left > right:
                return None
            middle = (left + right) // 2
            path[middle].left = construct_bst(left, middle - 1, path)
            path[middle].right = construct_bst(middle + 1, right, path)
            return path[middle]


        path = inorder_bts(root)
        return construct_bst(0, len(path) - 1, path)


if __name__ == "__main__":
    res = Solution().taskSchedulerII(tasks = [5,8,8,5], space = 2)
    print(res)
