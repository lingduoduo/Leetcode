class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.s = []
        self.traverse(root1)
        s1 = self.s
        self.s = []
        self.traverse(root2)
        s2 = self.s

        s = s1 + s2
        s.sort()
        return s

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        self.s.append(root.val)
        self.traverse(root.right)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res, s1, s2 = [], [], []
        while root1 or s1 or root2 or s2:
            while root1:
                s1.append(root1)
                root1 = root1.left
            while root2:
                s2.append(root2)
                root2 = root2.left

            if s1 and s2:
                if s1[-1].val <= s2[-1].val:
                    node = s1.pop()
                    res.append(node.val)
                    root1 = node.right
                else:
                    node = s2.pop()
                    res.append(node.val)
                    root2 = node.right
            elif not s1:
                node = s2.pop()
                res.append(node.val)
                root2 = node.right
            else:
                node = s1.pop()
                res.append(node.val)
                root1 = node.right
        return res
