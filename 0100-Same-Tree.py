###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ####First Try
        ###if p is None and q is None:
        ###	return True
        ###if p is None and q is not None:
        ###	return False
        ###if p is not None and q is None:
        ###	return False
        ###if p.val != q.val:
        ###	return False
        ###if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
        ###	return True
        ###return False
        
        ###if not p and not q:
        ###    return True
        ###if not p or not q:
        ###    return False
        ###if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
        ###    return True
        ###else:
        ###    return False
        
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        
        if p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
            
        
        


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    
    result = Solution().isSameTree(p, q)
    print(result)
