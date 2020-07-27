# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## First Try
        # if root is None:
        # 	return 0
        # if root.left is None and root.right is None:
        # 	return 1
        # leftDepth = minDepth(root.left)
        # rightDepth = minDepth(root.right)
        # if root.left is None:
        # 	return rightDepth+1
        # if root.right is None:
        # 	retrun leftDepth+1
        # return min(leftDepth, rightDepth)+1
        
        ## Second Try
        # if not root:
        #     return 0
        # left = float('inf')
        # right = float('inf')
        # if not root.left and not root.right:
        #     return 1
        # if root.left:
        #     left = self.minDepth(root.left)
        # if root.right:
        #     right = self.minDepth(root.right)
        # return min(left, right) + 1
        
        ## Third Try
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
            
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left and root.right:
            return min(left, right) + 1
        else:
            return max(left, right) + 1
        


if __name__ == "__main__":
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    result = Solution().minDepth(root)
    print(result)
