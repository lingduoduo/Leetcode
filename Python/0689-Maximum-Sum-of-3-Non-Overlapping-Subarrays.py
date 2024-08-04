class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        W = []  # array of sums of windows
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            if i >= k:
                curr_sum -= nums[i - k]
            if i >= k - 1:
                W.append(curr_sum)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, l
        return ans

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        p = [0] + list(accumulate(nums))
        a = [(u, u + k - 1, (p[u + k] - p[u])) for u in range(0, len(nums) - k + 1)]

        n, d = len(a), 3

        dp = [[-inf for _ in range(d + 1)] for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = 0

        h = defaultdict(list)
        for i in range(1, n + 1):
            for dd in range(1, d + 1):
                dp[i][dd] = max(dp[i][dd], dp[i - 1][dd])
                pv = (dp[i - k][dd - 1] if i - k >= 0 else 0)
                if dp[i][dd] < a[i - 1][2] + pv:
                    dp[i][dd] = a[i - 1][2] + pv
                    h[dp[i][dd]] = h[dp[i - k][dd - 1]] + [a[i - 1][0]]

        return h[dp[n][dd]]