import collections
from typing import List
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        pre = 0

        stack = [root]
        while stack:
            node = stack.pop()
            res = min(res, abs(node.val, pre))
            pre = node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    

    # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        pre = None
        stack = []
        node = root
        cnt = 0
        max_cnt = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left  
            node = stack.pop()
            if pre is not None:
                if pre.val == node.val:
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                        res = [node.val]
                    elif cnt == max_cnt:
                        res.append(node.val)
                else:
                    cnt = 0
            pre = node  
            node = node.right  
        return res