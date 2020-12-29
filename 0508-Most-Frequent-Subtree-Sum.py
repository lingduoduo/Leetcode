# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        d = []
        def counting(node):
            if not node:
                return 0
            
            left = counting(node.left)
            right = counting(node.right)
            d.append(left + right + node.val)
            return node.val + left + right
        
        counting(root)
        st = collections.Counter(d)
        max_cnt = max(st.values())
        return [k for k, v in st.items() if v == max_cnt ]
                     