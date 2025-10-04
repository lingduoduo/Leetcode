class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)

    def helper(self, word):
        res, d = [], {}
        for i, w in enumerate(word):
            if w not in d:
                d[w] = i
            res.append(d[w])
        return res

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for cs, ct in zip(s, t):
            if cs in map_s_t and map_s_t[cs] != ct:
                return False
            if ct in map_t_s and map_t_s[ct] != cs:
                return False
            map_s_t[cs] = ct
            map_t_s[ct] = cs

        return True

if __name__ == "__main__":
    s = "ab"
    t = "ca"
    result = Solution().isIsomorphic(s, t)
    print(result)
