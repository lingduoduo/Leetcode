###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def identicalTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if (
            p.val == q.val
            and self.identicalTree(p.left, q.right)
            and self.identicalTree(p.right, q.left)
        ):
            return True
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.issym(root.left, root.right)

    def issym(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False

        if (
            left.val == right.val
            and self.issym(left.left, right.right)
            and self.issym(left.right, right.left)
        ):
            return True
        else:
            return False


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        st = []  # 这里改成了栈
        st.append(root.left)
        st.append(root.right)
        while st:
            rightNode = st.pop()
            leftNode = st.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    result = Solution().isSymmetric(root)
    print(result)
