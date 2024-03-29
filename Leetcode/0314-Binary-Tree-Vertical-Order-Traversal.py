from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(list)
        
        stack = []
        stack.append((0, root))
        
        while stack:
            for i in range(len(stack)):
                pos, node = stack.pop(0)
                d[pos].append(node.val)
                if node.left:
                    stack.append((pos - 1, node.left))
                if node.right:
                    stack.append((pos + 1, node.right))
        return [v for k, v in sorted(d.items(), key=lambda x: x[0])]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = Solution().verticalOrder(root)
    print(res)
