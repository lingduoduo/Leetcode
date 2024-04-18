from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : (i + len(needle))] == needle:
                return i
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        next = [0] * len(needle)
        j = -1
        next[0] = j
        for i in range(1, len(needle)):
            while j >= 0 and needle[i] != needle[j + 1]:
                j = next[j]
            if needle[i] == needle[j + 1]:
                j += 1
            next[i] = j
        print(next)

        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        def getNext(s: str) -> List:
            next = [0] * len(s)
            j = 0
            for i in range(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = next[j - 1]
                if s[i] == s[j]:
                    j += 1
                next[i] = j
            return next

        next  = getNext(needle)
        j = 0
        for i in range(1, len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def get_next(s: str) -> List:
            next = [0] * len(s)
            j = 0
            for i in range(1,len(s)):
                while j > 0 and s[i] != s[j]:
                    j = next[j-1]
                if s[i] == s[j]:
                    j += 1
                next[i] = j
            return next

        j = 0
        next_pos = get_next(needle)
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next_pos[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1  
        return -1  

if __name__ == "__main__":
    res = Solution().strStr(haystack="sadbutsad", needle="sad")
    print(res)
