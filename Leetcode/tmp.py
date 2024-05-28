# Definition for a binary tree node.
import collections
from typing import Optional, List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if len(preorder) <= 1:
            return True
        idx = 1
        while idx < len(preorder) and preorder[0] > preorder[idx]:
            idx += 1
        return self.verifyPreorder(preorder[1:idx]) and self.verifyPreorder(preorder[idx + 1:])

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def helper(preorder, low, high):
            if not preorder:
                return True
            root = preorder[0]
            if root <= low or root >= high:
                return False
            idx = 1
            while idx < len(preorder) and preorder[idx] < root:
                idx += 1
            left_valid = helper(preorder[1:idx], low, root)
            right_valid = helper(preorder[idx:], root, high)
            return left_valid and right_valid

        return helper(preorder, float('-inf'), float('inf'))

if __name__ == '__main__':
    res = Solution().getFactors(n=12)
    print(res)


