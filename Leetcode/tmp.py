# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if node == None:
                return None

            if node == p:
                return p
            if node == q:
                return q

            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if right == None:
                return left
            elif left == None:
                return right
            else:
                return node

        result = dfs(root, p, q)
        if result == None or (result != p and result != q):
            return result
        else:
            if (result == p and dfs(result, q, q) == None) or (result == q and dfs(result, p, p) == None):
                return None
            else:
                return result


if __name__ == "__main__":
    res = Solution().numFriendRequests(ages=[16, 17, 18])
    print(res)
