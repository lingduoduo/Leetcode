##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def flatten(self, root):
        # """
        # :type root: TreeNode
        # :rtype: None Do not return anything, modify root in-place instead.
        # """
        ###    if not root:
        ###        return root
        #
        ###    dummy = TreeNode(-1)
        ###    self.last = dummy
        ###    self.dfs(root)
        ###    return dummy.right
        #
        ###def dfs(self, curr):
        ###    if not curr:
        ###        return
        #
        ###    self.last.right = TreeNode(curr.val)
        ###    self.last = self.last.right
        #
        ###    self.dfs(curr.left)
        ###    self.dfs(curr.right)
        
    #     self.nodes = list()
    #     self.dfs(root)
        
    #     dummy = TreeNode(-1)
    #     dummy.right = root
    #     curr = dummy
    #     while self.nodes:
    #         curr.right = self.nodes.pop(0)
    #         curr = curr.right
    #     return dummy.right
    
    # def dfs(self, root):
    #     if not root:
    #         return
    #     self.nodes.append(root)
    #     left = root.left
    #     right = root.right
    #     root.left = None
    #     root.right = None
    #     self.dfs(left)
    #     self.dfs(right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right
        
        root.left = None
        
        self.flatten(left)
        self.flatten(right)
        
        root.right = left
        curr = root

        while curr.right:
            print(curr.right.val)
            curr = curr.right
        curr.right = right

if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(5)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right.right = TreeNode(6)
    
    ###Solution().printTree(p)
    
    result = Solution().flatten(p)

