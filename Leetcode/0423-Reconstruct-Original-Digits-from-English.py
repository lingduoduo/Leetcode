class Solution:
    def originalDigits(self, s: str) -> str:
        cnts = collections.Counter(s)
        nums = [
            "six",
            "zero",
            "two",
            "eight",
            "seven",
            "four",
            "five",
            "nine",
            "one",
            "three",
        ]
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] // cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for i in range(t):
                cnts.subtract(cntn)
        return "".join(str(i) * n for i, n in enumerate(ans))
