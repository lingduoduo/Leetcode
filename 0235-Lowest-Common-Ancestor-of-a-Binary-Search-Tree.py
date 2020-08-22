class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pointer = root
        
        while pointer:
            if p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            elif p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            else:
                return pointer
