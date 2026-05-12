from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def get_next(s: str) -> List[int]:
            nxt = [0] * len(s)
            j = 0
            for i in range(len(s)):
                while j > 0 and s[i] != s[j]:
                    j = nxt[j - 1]
                
                if s[i] == s[j]:
                    j += 1
                
                nxt[i] = j
            return nxt
        
        
        nxt = get_next(needle)
        n = len(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j - 1]
            
            if haystack[i] == needle[j]:
                j += 1
            
            if j == n - 1:
                return i - n + 1
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def get_next(s):
            nxt = [0] * len(s)
            j = 0

            for i in range(1, len(s)):

                while j > 0 and s[i] != s[j]:
                    j = nxt[j - 1]

                if s[i] == s[j]:
                    j += 1

                nxt[i] = j

            return nxt

        nxt = get_next(needle)

        j = 0

        for i in range(len(haystack)):

            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == len(needle):
                return i - len(needle) + 1

        return -1


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern(s = "abcabcabcabc"))