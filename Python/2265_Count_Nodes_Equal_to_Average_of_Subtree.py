# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(root):
            nonlocal res
            if not root:
                return 0, 0
            if not root.left and not root.right:
                res += 1 
                return 1, root.val
            left_cnt, left_sum = traverse(root.left)
            right_cnt, right_sum = traverse(root.right)
            cnt = left_cnt + right_cnt
            tot = left_sum + right_sum
            if (tot + root.val)//(cnt + 1) == root.val:
                res += 1
            return cnt + 1, tot + root.val
        traverse(root)
        return res

        
