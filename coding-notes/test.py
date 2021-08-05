class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def treeTot(self, root, num):
        self.res = []
        self.backtracking(root, num, [])
        return self.res 

    def backtracking(self, node, target, path):
        print(path)
        if node == None:
            return

        path.append(node.val)
        target -= node.val

        if target == 0 and node.left == None and node.right == None:
            self.res.append(path[:])
        else:
            self.backtracking(node.left, target, path)
            self.backtracking(node.right, target, path)
        path.pop()

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)

    res = Solution().treeTot(root, 22)
    print(res)
