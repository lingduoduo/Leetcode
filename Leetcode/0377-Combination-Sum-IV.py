class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # 什么都不选也是一种方案
        for i in range(1, target + 1):
            # update dp[i]
            for num in nums:
                if i >= num: dp[i] += dp[i - num]  # i - x 不可以 < 0

        return dp[target]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]
        for i in range(1, target + 1):
            dp.append(sum([dp[i - n] for n in nums if n <= i]))
        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().combinationSum4(nums, 4)
    print(res)

    nums = [4, 2, 1]
    res = Solution().combinationSum4(nums, 32)
    print(res)
