class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = collections.defaultdict(collections.Counter)
        dp[-1][float("-inf")] = 1
        table = []
        for num in nums:
            i = bisect.bisect_left(table, num)
            if i == len(table):
                table.append(num)
            else:
                table[i] = num
            dp[i][num] += sum(dp[i - 1][j] for j in dp[i - 1] if j < num)
        return sum(dp[max(0, len(table) - 1)].values())
