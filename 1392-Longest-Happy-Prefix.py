class Solution:
    def longestPrefix(self, s: str) -> str:

        ###n = len(s)
        ###for i in range(n-1, 0, -1):
        ###    if s[:i] == s[-i:]:
        ###        return s[:i]
        ###return ""

        ###n = len(s)
        ###f = [0] * (n + 1)
        ###f[0], i, j = -1, 0, -1
        
        ###while i < n:
        ###    while j != -1 and s[i] != s[j]:
        ###        j = f[j]
        ###    i += 1
        ###    j += 1
        ###    f[i] = j
        ###return s[:f[-1]]


        m = len(s)
        nxt = [0, 0]
        j = 0
        for i in range(1, m):
            while j>0 and s[i] != s[j]:
                j = nxt[j]
            if s[i] == s[j]:
                j += 1
            nxt.append(j)
        print(nxt)
        return s[:nxt[-1]]


if __name__ == '__main__':
    strs = "level"
    result = Solution().longestPrefix(strs)
    print(result)