# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))

    def inOrder(self, root, res):
        if not root:
            return []
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)


class Solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None  # 记录前一个节点
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left  # 左
            else:
                cur = stack.pop()  # 中
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur  # 保存前一个访问的结点
                cur = cur.right  # 右
        return True


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def traverse(root, min_val, max_val):
            if root is None: return True
            if root.val <=  min_val or root.val >= max_val: return False
            return traverse(root.left, min_val, root.val) and traverse(root.right, root.val, max_val)
        
        return traverse(root, float("-inf"), float("inf"))