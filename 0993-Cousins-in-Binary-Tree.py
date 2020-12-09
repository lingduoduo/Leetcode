class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = {root.val: (0, None)}
        stack = [root]
        depth = 0
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                    d[node.left.val] = (depth + 1, node)
                if node.right:
                    stack.append(node.right)
                    d[node.right.val] = (depth + 1, node)
            depth += 1
            
        dx, px = d[x]
        dy, py = d[y]
        return dx == dy and px != py