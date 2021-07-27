class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root_idx = inorder.index(preorder[0])
        preorder_left = preorder[1:root_idx+1]
        inorder_left = inorder[:root_idx]

        preorder_right = preorder[root_idx+1:]
        inorder_right = inorder[root_idx+1:]

        left = self.buildTree(preorder_left, inorder_left)
        right = self.buildTree(preorder_right, inorder_right)

        return TreeNode(preorder[0], left, right)

if __name__ == '__main__':
    res = Solution().buildTree(preorder=[3, 9, 20, 15, 7], intorder=[9, 3, 15, 20, 7])


