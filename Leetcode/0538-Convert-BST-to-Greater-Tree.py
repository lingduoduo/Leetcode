# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.res = []

        self.inOrder(root, False)

        cum = 0
        for i in reversed(range(len(self.res))):
            cum += self.res[i]
            self.res[i] = cum

        self.inOrder(root, True)

        return root

    def inOrder(self, root, replacement):
        if not root:
            return

        if not replacement:
            self.inOrder(root.left, False)
            self.res.append(root.val)
            self.inOrder(root.right, False)
        else:
            self.inOrder(root.left, True)
            root.val = self.res.pop(0)
            self.inOrder(root.right, True)


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = []

        def traverse(root):
            nonlocal stack
            if not root:
                return
            if root.left:
                traverse(root.left)
            stack.append(root)
            if root.right:
                traverse(root.right)

        traverse(root)
        prev = 0
        while stack:
            node = stack.pop()
            prev += node.val
            node.val = prev
        return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.pre = 0  # 记录前一个节点的数值
        self.traversal(root)
        return root

    def traversal(self, cur):
        if cur is None:
            return
        self.traversal(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.traversal(cur.left)
