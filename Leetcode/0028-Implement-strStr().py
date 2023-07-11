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

        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1
