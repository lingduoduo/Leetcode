class Solution:
    def splitArray(self, nums, m) -> int:
        n = len(nums)
        self.sums = [0]*len(nums)
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1] + nums[i]
        self.dp = [[float("inf")]*n for _ in range(m)]
        return self.partial(nums, m)

    def partial(self, nums, m):
        k = len(nums) - 1
        if m == 1:
            return self.sums[k]
        if m > k + 1:
            return float("inf")
        if self.dp[m-1][k] != float("inf"):
            return self.dp[m-1][k]
        res = float("inf")
        for i in range(k):
            res = min(res, max(self.partial(nums[:i+1], m-1), self.sums[k]-self.sums[i]))
        self.dp[m-1][k] = res
        return res


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = [0]*n
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]

        dp = [[float("inf")]*n for _ in range(k)]
        for i in range(n):
            dp[0][i] = sums[i]

        for i in range(1, k):
            for j in range(i-1, n):
                for l in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][l], sums[j]-sums[l]))
        return dp[-1][-1]


class Solution:
    def splitArray(self, nums, m) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    count += 1

            if count > m:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    # nums = [1,2,3,4,5]
    # nums = [1,4,4]
    # nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
    results = Solution().splitArray(nums, 2)
    print(results)
