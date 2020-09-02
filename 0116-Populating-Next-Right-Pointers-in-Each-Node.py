"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
    #     self.d = dict()
    #     self.dfs(root, 0)
        
    #     for k in d.keys():
    #         for j in range(len(d[k])):
    #             if j == len(d[k]) - 1:
    #                 d[k][j].next = None
    #             else:
    #                 d[k][j].next = d[k][j + 1]
    #     return root
    
    # def dfs(self, root, level):
    #     if not root: return
    #     self.d[level] = self.d.get(level, []) + root
    #     self.dfs(root.left, level + 1)
    #     self.dfs(root.right, level + 1)

        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
