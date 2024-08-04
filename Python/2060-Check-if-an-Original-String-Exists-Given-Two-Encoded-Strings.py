class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        return self.dfs(s1, s2, 0, 0, 0)

    @lru_cache(None)
    def dfs(self, s1, s2, i, j, diff):
        if i == len(s1) and j == len(s2):
            return diff == 0
        if i < len(s1) and s1[i].isdigit():
            k = i
            val = 0
            while k < len(s1) and s1[k].isdigit():
                val = val * 10 + int(s1[k])
                k += 1
                if self.dfs(s1, s2, k, j, diff - val):
                    return True
        elif j < len(s2) and s2[j].isdigit():
            k = j
            val = 0
            while k < len(s2) and s2[k].isdigit():
                val = val * 10 + int(s2[k])
                k += 1
                if self.dfs(s1, s2, i, k, diff + val):
                    return True
        elif diff == 0:
            if (
                i < len(s1)
                and j < len(s2)
                and s1[i] == s2[j]
                and self.dfs(s1, s2, i + 1, j + 1, diff)
            ):
                return True
        elif diff > 0:
            if i < len(s1) and self.dfs(s1, s2, i + 1, j, diff - 1):
                return True
        elif diff < 0:
            if j < len(s2) and self.dfs(s1, s2, i, j + 1, diff + 1):
                return True
        return False


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def pos_len(s):
            """Return possible length"""
            ans = [int(s)]
            if len(s) == 2:
                if s[1] != '0': ans.append(int(s[0]) + int(s[1]))
                return ans
            elif len(s) == 3:
                if s[1] != '0': ans.append(int(s[:1]) + int(s[1:]))
                if s[2] != '0': ans.append(int(s[:2]) + int(s[2:]))
                if s[1] != '0' and s[2] != '0': ans.append(int(s[0]) + int(s[1]) + int(s[2]))
            return ans

        @cache
        def dp_fn(i, j, diff):
            """Return True if s1[i:] matches s2[j:] with given differences."""
            if i == len(s1) and j == len(s2): return diff == 0
            if i < len(s1) and s1[i].isdigit():
                ii = i
                while ii < len(s1) and s1[ii].isdigit(): ii += 1
                for x in pos_len(s1[i:ii]):
                    if dp_fn(ii, j, diff - x): return True
            elif j < len(s2) and s2[j].isdigit():
                jj = j
                while jj < len(s2) and s2[jj].isdigit(): jj += 1
                for x in pos_len(s2[j:jj]):
                    if dp_fn(i, jj, diff + x): return True
            elif diff == 0:
                if i == len(s1) or j == len(s2) or s1[i] != s2[j]: return False
                return dp_fn(i + 1, j + 1, 0)
            elif diff > 0:
                if i == len(s1): return False
                return dp_fn(i + 1, j, diff - 1)
            else:
                if j == len(s2): return False
                return dp_fn(i, j + 1, diff + 1)

        return dp_fn(0, 0, 0)