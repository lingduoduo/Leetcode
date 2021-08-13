class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root 

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and right:
            return right
        if not right and left:
            return left 
        if left and right:
            return root

if __name__ == '__main__':
    root = treeNode(4)
    root.left = treeNode(2)
    root.right = treeNode(6)
    root.left.left = treeNode(1)
    root.left.right = treeNode(3)
    root.right.left = treeNode(5)
    root.right.right = treeNode(7)

    res = Solution().lowestCommonAncestor(root, root.left.left, root.left.right)
    print(res.val)
