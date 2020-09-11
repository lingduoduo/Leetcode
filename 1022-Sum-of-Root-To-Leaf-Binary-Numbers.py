###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        self.dfs(root, [])
        val = 0
        while self.res:
            curr = 0
            seq = self.res.pop(0)
            for i in range(len(seq)):
                curr = curr * 2 + seq[i]
            val += curr
        return val
    
    def dfs(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            path = path + [root.val]
            self.res.append(path)
        
        self.dfs(root.left, path + [root.val])
        self.dfs(root.right, path + [root.val])


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(0)
    p.right = TreeNode(1)
    p.left.left = TreeNode(0)
    p.left.right = TreeNode(1)
    p.right.left = TreeNode(0)
    p.right.right = TreeNode(1)
    
    ###Solution().printTree(p)
    
    result = Solution().sumRootToLeaf(p)
    print(result)
