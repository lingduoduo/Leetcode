###Definition for a binary tree node.
###class TreeNode:
###    def __init__(self, val=0, left=None, right=None):
###        self.val = val
###        self.left = left
###        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == [] or inorder == []:
            return None

        rootval = preorder[0]
        root = TreeNode(rootval)
        inorderIdx = inorder.index(rootval)

        root.left = self.buildTree(preorder[1 : inorderIndex + 1], inorder[:inorderIdx])
        root.right = self.buildTree(
            preorder[inorderIndex + 1 :], inorder[inorderIdx + 1 :]
        )

        return root
