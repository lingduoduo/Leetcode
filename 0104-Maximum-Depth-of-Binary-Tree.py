# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## First Try
        # if root is None:
        # 	return 0
        # leftdepth = self.maxDepth(root.left)
        # rightdepth = self.maxDepth(root.right)
        # return max(leftdepth, rightdepth)+1
        
        ## Second Try
        # if not root:
        #     return 0
        # left = 0
        # right = 0
        # if root.left:
        #     left = self.maxDepth(root.left)
        # if root.right:
        #     right = self.maxDepth(root.right)
        # return max(left, right) + 1
        
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # if not root.left:
        #     return 1+self.maxDepth(root.right)
        # if not root.right:
        #     return 1+self.maxDepth(root.left)
        # return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right)+1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().maxDepth(root)
    print(result)
