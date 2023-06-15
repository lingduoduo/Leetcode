import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ###c1 = collections.Counter(s)
        ###c2 = collections.Counter(t)
        ###if c1 == c2:
        ###    return True
        ###else:
        ###    return False

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


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    results = Solution().isAnagram(s, t)
    print(results)
