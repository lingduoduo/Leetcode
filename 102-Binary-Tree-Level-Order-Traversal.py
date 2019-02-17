# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        level = 0
        
        def bfs(root, level):
            if root is None: return
            if len(result)==level: 
                result.append([])
            result[level].append(root.val)
            bfs(root.left, level+1)
            bfs(root.right, level+1)
        
        bfs(root, 0)
        return result