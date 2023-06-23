from typing import List


class Solution(object):
    def _partition(self, s, index, t, result):
        if index == len(s):
            result.append(t.copy())
            return

        for i in range(index + 1, len(s) + 1):
            if s[index:i] == s[index:i][::-1]:
                t.append(s[index:i])
                self._partition(s, i, t, result)
                t.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        if not s:
            return result

        self._partition(s, 0, list(), result)
        return result


class Solution(object):
    def partition(self, s):
        self.res = []
        self.helper(s, [])
        return self.res

    def dfs(self, s, path):
        if len(s) == 0:
            self.res.append(path)
            return

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path + [s[:i]])


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(strs, path):
            nonlocal res
            print(strs, path)
            if len(strs) == 1:
                res.append(path)
                return

            for i in range(1, 1 + len(strs)):
                if strs[:i] == strs[:i][::-1]:
                    dfs(strs[i:], path + [strs[:i]])

        res = []
        dfs(s, [])
        return res


if __name__ == "__main__":
    res = Solution().partition(s="aab")
    print(res)
