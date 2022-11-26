# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root.val:None}
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                parents[node.left.val] = node
                stack.append(node.left)
            if node.right:
                parents[node.right.val] = node
                stack.append(node.right)
        ancestors = set()
        if p.val not in parents or q.val not in parents: return None
        while p:
            ancestors.add(p.val)
            p = parents[p.val]
        while q and q.val not in ancestors:
            q = parents[q.val]
        return q

if __name__ == "__main__":

    res = Solution().lowestCommonAncestor(root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1)
    print(res)