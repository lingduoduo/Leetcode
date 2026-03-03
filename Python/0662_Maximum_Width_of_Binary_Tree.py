from collections import deque

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])  # (node, index)
        res = 0

        while q:
            level_len = len(q)
            _, first = q[0]
            _, last = q[-1]
            res = max(res, last - first + 1)

            for _ in range(level_len):
                node, idx = q.popleft()
                idx -= first  # normalize to keep numbers small
                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))

        return res

if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    p.left.right = TreeNode(5)
    p.right.right = TreeNode(9)

    result = Solution().widthOfBinaryTree(p)
    print(result)
