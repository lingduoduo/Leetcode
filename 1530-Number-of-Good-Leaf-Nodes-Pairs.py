# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
    	if not root:
    		return []

    	self.result = []
    	self.dfs(root)
    	return self.result


    def dfs(self, root):
    	if not root:
    		return

    	self.dfs(root.left)

    	self.dfs(root.right)

    	self.result.append(root.val)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    root.left.left = TreeNode(4)
    root.left.right = None
    
    root.right.left = None
    root.right.right = TreeNode(6)
    
    result = Solution().countPairs(root, 0)
    print(result)
