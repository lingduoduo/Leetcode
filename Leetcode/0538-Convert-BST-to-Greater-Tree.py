class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
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