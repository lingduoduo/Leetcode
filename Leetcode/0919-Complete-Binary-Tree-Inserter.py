from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections

class CBTInserter:
    def __init__(self, root: TreeNode):
        self.tree = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            self.tree.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        n = len(self.tree)
        parent = self.tree[(n - 1) // 2]
        node = TreeNode(v)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
        self.tree.append(node)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.tree[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = [root]
        for i in self.tree:
            if i.left: self.tree.append(i.left)
            if i.right: self.tree.append(i.right)

    def insert(self, val: int) -> int:
        n = len(self.tree)
        self.tree.append(TreeNode(val))
        if n % 2:
            self.tree[(n - 1) // 2].left = self.tree[-1]
        else:
            self.tree[(n - 1) // 2].right = self.tree[-1]
        return self.tree[(n - 1) // 2].val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()