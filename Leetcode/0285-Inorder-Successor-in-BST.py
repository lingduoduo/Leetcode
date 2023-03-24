class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > p.val:
            return self.inorderSuccessor(root.left,p) or root
        return self.inorderSuccessor(root.right,p)