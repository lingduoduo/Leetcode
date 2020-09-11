###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def identicalTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val and self.identicalTree(p.left, q.right) and self.identicalTree(p.right, q.left):
            return True
        return False
    
    def isSymmetric(self, root):
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        ####First Try
        ###def dfs(left, right):
        ###	if left is None and right is None:
        ###		return True
        ###	if left is None:
        ###		return False
        ###	if right is None:
        ###		return False
        ###	flag1 = dfs(left.left, right.left)
        ###	flag2 = dfs(left.right, right.right)
        ###	if left.val == right.val and flag1  and flag2:
        ###		return True
        
        ###if root is None:
        ###      	return True
        ###      if root.left is None and root.right is None:
        ###      	return True
        ###      if root.left is None and root.right is not None:
        ###      	return False
        ###      if root.left is not None and root.right is None:
        ###      	return False
        ###      return True if dfs(root.left, root.right) False
        
        ####Second Try
        if not root:
            return True
        
        return self.issym(root.left, root.right)
    
    def issym(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False
        
        if left.val==right.val and self.issym(left.left, right.right) and self.issym(left.right, right.left):
            return True
        else:
            return False
       

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    
    result = Solution().isSymmetric(root)
    print(result)
