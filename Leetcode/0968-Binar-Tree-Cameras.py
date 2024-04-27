from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node, par):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered) or (node.left not in covered or node.right not in covered):
                    self.res += 1
                    covered.update({node, par, node.left, node.right})

        self.res = 0
        covered = {None}
        dfs(root, None)
        return self.res


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = [0]  

        def traversal(cur: TreeNode, result: List[int]) -> int:
            if not cur:
                return 2

            left = traversal(cur.left)
            right = traversal(cur.right)

            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                result[0] += 1
                return 1
            else:
                return 2
            
        if traversal(root, result) == 0:
            result[0] += 1

        return result[0]