###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.result = 0
        
        def DFS(root, k):
            if root is None:
                return
            DFS(root.left, k)
            self.cnt += 1
            if self.cnt == k:
                self.result = root.val
            DFS(root.right, k)
        
        DFS(root, k)
        return self.result
