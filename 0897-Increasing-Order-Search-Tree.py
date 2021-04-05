# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.vals = []
        self.trav(root)
        
        for idx, val in enumerate(self.vals):
            if idx == 0:
                curr = TreeNode(val)
                dummy = curr
            else:
                curr.right = TreeNode(val)
                curr = curr.right
        return dummy
    
    def trav(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.vals.append(root.val)
            return
        self.trav(root.left)
        self.vals.append(root.val)
        self.trav(root.right)
        return
        