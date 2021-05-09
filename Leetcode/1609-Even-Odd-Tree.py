class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        level = 0
        stack = [root]
        while stack:
            next_level = []
            prev_num = None
            for cur_node in stack:
                if level % 2 == 0:
                    if cur_node.val % 2 == 0:
                        return False
                    if prev_num is not None and cur_node.val <= prev_num:
                        return False
                    prev_num = cur_node.val
                else:
                    if cur_node.val % 2 != 0:
                        return False
                    if prev_num is not None and cur_node.val >= prev_num:
                        return False
                    prev_num = cur_node.val
                if cur_node.left is not None:
                    next_level.append(cur_node.left)
                if cur_node.right is not None:
                    next_level.append(cur_node.right)
            stack = next_level
            level += 1
        return True  


if __name__ == '__main__':
    root = TreeNode(1, None, None)
    root.left = TreeNode(10, None, None)
    root.right = TreeNode(4, None, None)

    root.left.left = TreeNode(3, None, None)
    root.right.left = TreeNode(7,  None, None)
    root.right.right = TreeNode(9, None, None)

    root.left.left.left = TreeNode(12, None, None)
    root.left.left.right = TreeNode(8, None, None)

    root.right.left.left = TreeNode(6, None, None)
    root.right.right.right = TreeNode(2, None, None)
    res = Solution().isEvenOddTree(root)
    print(res)
    [1,10,4,3,null,7,9,12,8,6,null,null,2]
    [11,18,14,3,7,null,null,null,null,18,null,6]

