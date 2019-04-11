# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Firs Recursive solution
        if root is None:
            return []
        result = list()

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)

        dfs(root)
        return result

        # ## Second recursive solution
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res

        # iterative solution
        stack = []
        result = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                return result
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        # Third try
        if not root:
            return root
        visited = []
        res = []
        curr = root

        while True:
            while curr:
                visited.append(curr)
                curr = curr.left
            if not visited:
                return res
            curr = visited.pop()
            res.append(curr.val)
            curr = curr.right
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    result = Solution().inorderTraversal(root)
    print(result)
