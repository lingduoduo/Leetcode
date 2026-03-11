class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s

        alt1 = ""
        alt2 = ""
        for i in range(2 * n):
            alt1 += '0' if i % 2 == 0 else '1'   # 010101...
            alt2 += '1' if i % 2 == 0 else '0'   # 101010...

        diff1 = diff2 = 0
        left = 0
        res = float("inf")

        for right in range(2 * n):
            if ss[right] != alt1[right]:
                diff1 += 1
            if ss[right] != alt2[right]:
                diff2 += 1

            if right - left + 1 > n:
                if ss[left] != alt1[left]:
                    diff1 -= 1
                if ss[left] != alt2[left]:
                    diff2 -= 1
                left += 1

            if right - left + 1 == n:
                res = min(res, diff1, diff2)

        return res
