###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True

        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        if left or right:
            return True
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        st = [(root, root.val)]
        while st:
            node, path_sum = st.pop()
            if not node.left and not node.right and path_sum == sum:
                return True
            if node.right:
                st.append((node.right, path_sum + node.right.val))
            if node.left:
                st.append((node.left, path_sum + node.left.val))
        return False


if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    ###root.left.left = TreeNode(3)
    ###root.left.right = TreeNode(4)

    result = Solution().hasPathSum(root, 10)
    print(result)
