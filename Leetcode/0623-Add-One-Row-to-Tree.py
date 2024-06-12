from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            dummy = TreeNode(v, root, None)
            return dummy

        nodes = []

        def travese(r, d):
            if not r:
                return
            if d == 0:
                nodes.append(r)
                return
            travese(r.left, d - 1)
            travese(r.right, d - 1)

        travese(root, d - 2)
        for node in nodes:
            node.left = TreeNode(v, node.left, None)
            node.right = TreeNode(v, None, node.right)
        return root


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        bfs = deque([root])
        while bfs and depth != 1:
            size = len(bfs)
            depth -= 1
            for _ in range(size):
                curr = bfs.popleft()
                if curr.left != None:
                    bfs.append(curr.left)
                if curr.right != None:
                    bfs.append(curr.right)

                if (
                    depth == 1
                ):  # Current level is in depth d-1 -> Add nodes with value `v`
                    curr.left = TreeNode(val, curr.left, None)
                    curr.right = TreeNode(val, None, curr.right)
        return root


if __name__ == "__main__":
    root = TreeNode(4, None, None)
    root.left = TreeNode(2, None, None)
    root.right = TreeNode(6, None, None)
    root.left.left = TreeNode(3, None, None)
    root.left.right = TreeNode(1, None, None)
    root.right.left = TreeNode(5, None, None)
    res = Solution().addOneRow(root, 1, 2)
