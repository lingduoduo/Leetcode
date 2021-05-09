# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.preOrder(root)
        return ' '.join(map(str, self.res))
    
    def preOrder(self, root):
        if not root:
            return
        self.res.append(root.val)
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(val) for val in data.split()]
        return self.buildTree(data)

    def buildTree(self, data):
        if not data:
            return None
        if len(data) == 1:
            return TreeNode(data[0])
        else:
            left = []
            right = []
            for i in range(1, len(data)):
                if data[i] < data[0]:
                    left.append(data[i])
                else:
                    right.append(data[i])
            root = TreeNode(data[0])
            root.left = self.buildTree(left)
            root.right = self.buildTree(right)
            return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans