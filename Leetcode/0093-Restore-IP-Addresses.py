from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s and len(path) == 4:
            self.res.append(".".join(path))
            return

        for i in range(1, 4):
            if i > len(s):
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], path + [s[:i]])


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        def dfs(strs, path):
            nonlocal res
            if len(path) == 4 and len(strs) == 0:
                res.append('.'.join(path))
                return

            for i in range(1, 4):
                if i > len(strs):
                    continue
                number = int(strs[:i])
                if str(number) == strs[:i] and number <= 255:
                    dfs(strs[i:], path + [strs[:i]])

        res = []
        dfs(s, [])
        return res


if __name__ == "__main__":
    res = Solution().restoreIpAddresses(s="25525511135")
    print(res)
