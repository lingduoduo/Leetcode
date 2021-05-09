class Solution:
    def findContentChildren(self, g, s) -> int:
        result = 0
        g.sort()
        s.sort()
        j = 0
        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j < len(s) and s[j] >= g[i]:
                result += 1
                j += 1
        return result

if __name__ == "__main__":
    # g = [1, 2, 3]
    # s = [1, 1]
    # print(Solution().findContentChildren(g, s))
    
    a = [1, 2, 3]
    b = [1, 2]
    print(Solution().findContentChildren(a, b))
