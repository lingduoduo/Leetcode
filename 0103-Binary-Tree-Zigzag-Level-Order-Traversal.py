# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, res = [(root, 1)], []

        if not root:
        	return res

        while queue != []:
        	node, level = queue.pop(0)
        	if node.left:
        		queue.append((node.left, level+1))
        	if node.right:
        		queue.append((node.right, level+1))

        	if level == len(res):
        		res[level-1].append(node.val)
        	else:
        		res.append([node.val])

        for i in range(len(res)):
        	if i%2 == 1:
        		res[i]=res[i][::-1]

        return res

