# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
    
        d = collections.defaultdict(list)

        def bfs(root):
            stack = [root]
            level = 0

            while stack:
                for i in range(len(stack)):
                    node = stack.pop(0)
                    d[level].append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                level += 1
            return level
        
        l = bfs(root)
        
        return d[l-1][0]
