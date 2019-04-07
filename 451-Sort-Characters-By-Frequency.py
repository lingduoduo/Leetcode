class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()

        res = ''
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        for key in sorted(d, key=d.get, reverse=True):
            res += ''.join([key] * d[key])

        return res


if __name__ == '__main__':
    s = "tree"
    s = "cccaaa"
    s = "Aabb"
    result = Solution().frequencySort(s)
    print(result)
