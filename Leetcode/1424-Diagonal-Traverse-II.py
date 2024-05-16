# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        def inOrder(root):
            if not root:
                return
            node = root
            stack = []
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                self.stack.append(node.val)
                node = node.right

if __name__ == "__main__":
    res = Solution().findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(res)
