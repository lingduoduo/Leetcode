# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.getHeight(root)
        w = 2 ** h - 1
        result = [[" " for _ in range(w)] for _ in range(h)]
        # self.fillValue(root, result, 0, 0, w-1)
        return result

     def getHeight(self, root):
		if root == None:
			return 0
		return max(self.getHeight(root.left),
                   self.getHeight(root.right))+1

	def fillValue(self, root, result, h, l, r):
		if root == None:
			return 0
		mid = (l+r-1)/2
		result[h][mid] = str(root.val)
		self.fillValue(root.left, result, h+1, l, mid-1)
		self.fillValue(root.right, result, h+1, mid+1, r)

if __name__== "__main__":
	print(Solution().matrixReshape([[1,2],[3,4]], 4, 1))

