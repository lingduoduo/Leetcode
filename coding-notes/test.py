class treeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        self.res  = True
        self.height
        return self.res

    def height(self, root):
        if not root or not self.res:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) <= 1:
            self.res = True
        else:
            self.res = False
        return 1 + max(left, right) 

    
if __name__ == '__main__':
    root = treeNode(5)
    root.left = treeNode(3)
    root.right = treeNode(7)
    root.left.left = treeNode(2)
    root.left.right = treeNode(4)
    root.right.left = treeNode(6)
    root.right.right = treeNode(8)

    res = Solution().isBalanced(root)
    print(res)
  

# ```java
# private boolean isBalanced = true;

# public boolean IsBalanced_Solution(TreeNode root) {
#     height(root);
#     return isBalanced;
# }

# private int height(TreeNode root) {
#     if (root == null || !isBalanced)
#         return 0;
#     int left = height(root.left);
#     int right = height(root.right);
#     if (Math.abs(left - right) > 1)
#         isBalanced = false;
#     return 1 + Math.max(left, right);
# }
# ```