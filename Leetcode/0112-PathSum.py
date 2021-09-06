###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ###First Try
        ###if root is None:
        ###	return False
        ###if root.left is None and root.right is None and root.val == sum:
        ###	return True
        ###if self.hasPathSum(root.left, sum-root.val):
        ###	return True
        ###if self.hasPathSum(root.right, sum-root.val):
        ###	return True
        ###return False
        
        ###Second Try
        ###if not root:
        ###    return False
        ###if not root.left and not root.right and root.val == sum:
        ###    return True
        ###left = right = False
        ###if root.left:
        ###    left = self.hasPathSum(root.left, sum-root.val)
        ###if root.right:
        ###    right = self.hasPathSum(root.right, sum-root.val)
        ###return left or right
        
        ###Third Try
        ###if not root:
        ###    return False
        #
        ###if not root.left and not root.right:
        ###    return root.val == sum
        #
        ###return self.hasPathSum(
        ###    root.left,
        ###    sum -
        ###    root.val) or self.hasPathSum(
        ###    root.right,
        ###    sum -
        ###    root.val)
        
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        
        left = self.hasPathSum(root.left, sum-root.val)
        right = self.hasPathSum(root.right, sum-root.val)
        if left or right:
            return True
        return False

    ###def dfs(self, root, target):   
    ###    if not root:
    ###        return False
        
    ###    if not root.left and not root.right and root.val == target:
    ###        return True
        
    ###    if root.left: 
    ###        left = self.dfs(root.left, target-root.val)
    ###    if root.right:
    ###        right = self.dfs(root.right, target-root.val)
    ###    if left or right:
    ###        return True
    ###    return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        if root.left and self.hasPathSum(root.left, targetSum - root.val):
            return True

        if root.right and self.hasPathSum(root.right, targetSum - root.val):
            return True

        return False

if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    ###root.left.left = TreeNode(3)
    ###root.left.right = TreeNode(4)

    result = Solution().hasPathSum(root, 10)
    print(result)

