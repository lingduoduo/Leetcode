##Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(root):
            if not root:
                return None

            res.append(root)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        dummy = TreeNode(-1)
        p = dummy

        for node in res:
            p.right = node
            node.left = None
            p = node
        return dummy.right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        root.left = None

        self.flatten(left)
        self.flatten(right)

        root.right = left
        while root.right:
            root = root.right
        root.right = right


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(5)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right.right = TreeNode(6)

    result = Solution().flatten(p)
