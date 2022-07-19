###Definition for a binary tree node.
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
        ###Firs Recursive solution
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


class Solution(object):
    def inorderTraversal(self, root):
        #######Second recursive solution
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res


class Solution(object):
    def inorderTraversal(self, root):
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


class Solution(object):
    def inorderTraversal(self, root):
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


class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []

        stack = []
        res = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
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
