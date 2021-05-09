# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.res = []
        
        self.inOrder(root, False)

        cum = 0
        for i in reversed(range(len(self.res))):
            cum += self.res[i]
            self.res[i] = cum

        self.inOrder(root, True)

        return root

    def inOrder(self, root, replacement):
        if not root:
            return

        if not replacement:
            self.inOrder(root.left, False)
            self.res.append(root.val)
            self.inOrder(root.right, False)
        else:
            self.inOrder(root.left, True)
            root.val = self.res.pop(0)
            self.inOrder(root.right, True)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    results = Solution().bstToGst(root)
    print(results)