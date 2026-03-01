# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cnt):
            if not node: return 0

            if node.left:
                if node.left.val == node.val:
                    left = dfs(node.left, cnt + 1)
                else:
                    left = dfs(node.left, cnt)
            
            if node.right:
                if node.right.val == node.val:
                    right = dfs(node.right, cnt + 1)
                else:
                    right = dfs(node.right, cnt)
            
            if node.left and node.right:
                if node.left.val == node.right.val:
                    return left + right
                else:
                    return max(left, right)
            else:
                return left or right
        
        dfs(root, 0)