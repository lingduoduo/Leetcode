class Solution:
    def getMost(self, strs) -> int:
        cur = 0
        res = 0
        preindex = [-1] * 26

        for i, cha in enumerate(strs):
            idx = ord(cha) - ord("a")
            if preindex[idx] == -1 or i - preindex[idx] > cur:
                cur += 1
            else:
                res = max(res, cur)
                cur = i - preindex[idx]
            preindex[idx] = i
        return res

if __name__ == '__main__':
    res = Solution().getMost(strs="arabcacfr")
    print(res)

