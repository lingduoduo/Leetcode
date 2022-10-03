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
            if i < len(s1) and j < len(s2) and s1[i] == s2[j] and self.dfs(s1, s2, i + 1, j + 1, diff):
                return True
        elif diff > 0:
            if i < len(s1) and self.dfs(s1, s2, i + 1, j, diff - 1):
                return True
        elif diff < 0:
            if j < len(s2) and self.dfs(s1, s2, i, j + 1, diff + 1):
                return True
        return False