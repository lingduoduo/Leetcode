# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

    self.res = 0

    def dfs(self, root):
        if not root:
            return

        self.res += 1

        self.dfs(root.left)
        self.dfs(root.right)
            
    #     left_height = self.get_height(root.left)
    #     right_height = self.get_height(root.right)
    #     if left_height == right_height:
    #         nodes = 2 ** left_height + self.countNodes(root.right)
    #     else:
    #         nodes = 2 ** right_height + self.countNodes(root.left)
    #     return nodes


    # def get_height(self, root, height):
    #     if not root:
    #         return 0

    #     left = self.get_height(root.left, height+1)
    #     right = self.get_height(root.right, height+1)
    #     return max(1+left, 1+right)

