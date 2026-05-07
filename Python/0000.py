from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i + 1):
                if i == j:
                    dp[j][i] = True
                elif i - j == 1 and s[i] == s[j]:
                    dp[j][i] == True
                elif i - j > 1 and s[i] == s[j] and dp[j + 1][i - 1]:
                    dp[j][i] = True
                    res += 1
        return res
        
if __name__ == "__main__":
    print(Solution().numTrees(n=3))