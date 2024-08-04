import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in d:
                return False
            else:
                d[t[j]] -= 1

        val = [v for v in d.values()]
        return val == [0] * len(val)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                # record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = [0] * 26
        for i in s:
            h[ord(i) - ord("a")] += 1
        for i in t:
            h[ord(i) - ord("a")] -= 1
        return all(i == 0 for i in h)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    results = Solution().isAnagram(s, t)
    print(results)

    s = "rat"
    t = "car"
    results = Solution().isAnagram(s, t)
    print(results)
