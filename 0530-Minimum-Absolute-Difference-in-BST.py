###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
    ###    s = list()
    ###    self.inorder(root, s)
    ###    result = s[1] - s[0]
    ###    for i in range(2, len(s)):
    ###        result = min(result, s[i] - s[i - 1])
    ###    return result
    
    ###def inorder(self, root, ss):
    ###    if root is None:
    ###        return
    ###    if root.left is None and root.right is None:
    ###        ss.append(root.val)
    ###        return
    ###    self.inorder(root.left, ss)
    ###    ss.append(root.val)
    ###    self.inorder(root.right, ss)
        
    ###    res = []
    ###    self.inorder(root, res)

    ###    min_abs = float("inf")
    ###    for i in range(1, len(output)):
    ###        min_abs = min(min_abs, output[i] - output[i-1]):
    ###    return min_abs


    ###def inorder(root, res):
    ###    if not root:
    ###        return
    ###    else:
    ###        self.inorder(root.left, res)
    ###        res.append(root.val)
    ###        self.inorder(root.right, res)

        self.res = float("inf")
        self.prev = None
        self.inOrder(root)
        return self.res

    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        if self.prev:
            self.res = min(self.res, self.root.val-self.prev.val)
        self.prev = root
        self.inOrder(root.right)