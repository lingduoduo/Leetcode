# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = list()
        q.append(root)
        idx = list()
        idx.append(1)
        result = 0
        
        while q:
            size = len(q)
            
            for i in range(size):
                node = q.pop(0)
                index = idx.pop(0)
                if i == 0:
                    left = index
                if i == size - 1:
                    right = index
                
                if node.left:
                    q.append(node.left)
                    idx.append(index * 2)
                if node.right:
                    q.append(node.right)
                    idx.append(index * 2 + 1)
            result = max(result, right - left + 1)
        return result


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    p.left.right = TreeNode(5)
    p.right.right = TreeNode(9)
    
    result = Solution().widthOfBinaryTree(p)
    print(result)
