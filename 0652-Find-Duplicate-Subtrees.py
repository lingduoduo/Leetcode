# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        m = collections.defaultdict(int)
        self.helper(root, m, res)
        return res

    def helper(self, root,  m, res):
        if not root:
            return '#'
        serialization = str(root.val) + ',' + self.helper(root.left, m, res) + ',' + self.helper(root.right, m, res)
        if m[serialization] == 1:
            res.append(root)
        m[serialization] += 1
        return serialization