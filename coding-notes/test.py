class treeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None


class Solution:
    def treeDepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.treeDepth(root.left), self.treeDepth(root.right)) 

    
if __name__ == '__main__':
    root = treeNode(5)
    root.left = treeNode(3)
    root.right = treeNode(7)
    root.left.left = treeNode(2)
    root.left.right = treeNode(4)
    root.right.left = treeNode(6)
    root.right.right = treeNode(8)

    res = Solution().treeDepth(root)
    print(res)
  
