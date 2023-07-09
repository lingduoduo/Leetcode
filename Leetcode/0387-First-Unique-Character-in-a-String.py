import collections


class Solution(object):
    def firstUniqChar(self, s):
        d = collections.Counter(s)

        for i, cha in enumerate(s):
            if d[cha] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i + 1 :]:
                return i

        return -1


if __name__ == "__main__":
    ###s = "leetcode"
    s = "loveleetcode"
    ###s = "cc"
    results = Solution().firstUniqChar(s)
    print(results)
