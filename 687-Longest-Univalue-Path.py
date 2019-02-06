# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def univalue(root):
        	if root is None: return 0

        	right = univalue(root.right)
        	left = univalue(root.left)
        	right_result = 0
        	left_result = 0

        	if root.right and root.val == root.right.val:
        		right_result = right+1

        	if root.left and root.val == root.left.val:
        		left_result = left+1

        	self.result = max(self.result, left_result+right_result)
        	return max(left_result, right_result)

        univalue(root)
        return self.result

        longest = [0]
        def dfs(root):
            if not root:
                return 0
            left_len, right_len = dfs(root.left), dfs(root.right)
            left = left_len + 1 if root.left and root.left.val == root.val else 0
            right = right_len + 1 if root.right and root.right.val == root.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        dfs(root)
        return longest[0]
