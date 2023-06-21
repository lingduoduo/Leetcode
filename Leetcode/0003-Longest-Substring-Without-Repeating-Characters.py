class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) <= 1:
            return 1
        longest = 0
        start = -1
        location = [-1 for i in range(256)]

        for i, v in enumerate(s):
            if location[ord(v)] > start:
                start = location[ord(v)]
            longest = max(longest, i - start)
            location[ord(v)] = i
        return longest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if len(s) <= 1:
            return 1

        result = 0
        left = -1
        n = len(s)
        d = {}

        for i in range(len(s)):
            if s[i] in d and d[s[i]] > left:
                left = d[s[i]]
            d[s[i]] = i
            result = max(result, i - left)
        return result


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dict = {}
        start = -1
        res = 0
        for j in range(len(s)):
            if s[j] in dict.keys() and dict[s[j]] > start:
                start = dict[s[j]]
            dict[s[j]] = j
            res = max(res, j - start)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = res = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
                res = max(res, i - start + 1)
            else:
                start = max(start, d[c] + 1)
                d[c] = i
                res = max(res, i - start + 1)
        return res


if __name__ == "__main__":
    result = Solution().lengthOfLongestSubstring("abcabcbb")
    print(result)
    result = Solution().lengthOfLongestSubstring("au")
    print(result)
    result = Solution().lengthOfLongestSubstring("abba")
    print(result)
