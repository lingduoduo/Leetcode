###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
       result = []
       self.DFS(root, result, 0)
       return result[::-1]
    
    def DFS(self, root, result, level):
       if not root: return

       self.DFS(root.left, res, level + 1)
       self.DFS(root.right, res, level + 1)
       if level >= len(result):
           result.append([])
       result[level].append(root.val)


class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        self.res = []
        self.dfs(root, 0)
        return self.res[::-1]
    
    
    def dfs(self, root, level):
        if not root:
            return

        if level >= len(self.res):
            self.res.append([])
        self.res[level].append(root.val)
        
        if root.left:
            self.dfs(root.left, level+1)
        if root.right:
            self.dfs(root.right, level+1)
            

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        res = []
        curr = root
        
        while curr:
            next_level, vals = [], []
            for node in curr:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr = next_level
            res.append(vals)
        
        return res[::-1]

    