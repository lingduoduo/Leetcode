# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if abs(l - r) > 1:
            self.res = False
        return 1 + max(l, r)
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def depth(root):
            if not root:
                return 0

            if not root.left and not root.right:
                return 1

            left = depth(root.left) if root.left else 0
            right = depth(root.right) if root.right else 0
            return max(left, right) + 1
            
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
