# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.inOrder(root)

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        self.stack.append(root.val)
        self.inOrder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.do_left(root)

    def do_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        ret = self.stack.pop()
        if ret.right:
            self.do_left(ret.right)
        return ret.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
