# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def preOrder(self, root):
        if not root:
            self.vals.append("#")
        else:
            self.vals.append(str(root.val))
            self.preOrder(root.left)
            self.preOrder(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.vals = []
        self.preOrder(root)
        return " ".join(self.vals)

    def build(self, vals):
        if not vals:
            return None

        val = vals.popleft()
        if val == "#":
            return None
        root = TreeNode(int(val))
        root.left = self.build(vals)
        root.right = self.build(vals)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split())
        return self.build(vals)
