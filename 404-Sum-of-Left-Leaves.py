# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sumofLeftLeaves(tree):
    """
  :type root: TreeNode
  :rtype: int
  """
    if tree == None:
        return 0
    sum = 0
    if tree.left != None and tree.right != None:
        sum += tree.left.val
    return (sum + sumofLeftLeaves(tree.left) + sumofLeftLeaves(tree.right))


def sumOfLeftLeaves(self, root):
    
    
    """
    :type root: TreeNode
    :rtype: int
    """
if root == None:
    return 0

sum = 0
if root.left != None and root.left.left == None and root.left.right == None:
    sum += root.left.val

return sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    self.result = 0
    
    def trav(root):
        if not root:
            return
        
        if root.left and not root.left.left and not root.left.right:
            self.result += root.left.val
        
        trav(root.left)
        trav(root.right)
    
    trav(root)
    return self.result
