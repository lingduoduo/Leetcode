###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ###if not root:
        ###    return None
        #
        ###root.left, root.right = root.right, root.left
        ###self.invertTree(root.left)
        ###self.invertTree(root.right)
        ###return root

        # if not root:
        #     return None
        # if not root.left and not root.right:
        #     return root
        # root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        # return root

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root
