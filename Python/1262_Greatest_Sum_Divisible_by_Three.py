from typing import List

class Solution:
    def maxSumDivThree(self, nums):
        from collections import defaultdict

        dic = defaultdict(list)

        nums.sort()

        for num in nums:
            dic[num % 3].append(num)

        s = sum(nums)
        if s % 3 == 0:
            return s

        if s % 3 == 2:
            t1, t2 = float("inf"), float("inf")
            if 2 in dic:  # 可以删除一个模为 2 的最小数
                t1 = dic[2][0]

            if len(dic[1]) >= 2:  # 也可以删除模为 1 的最小的两个数
                t2 = dic[1][0] + dic[1][1]

            if t1 > t2:  # 选择两种可能中较小的值删除
                return s - t2

            return s - t1

        if s % 3 == 1:
            t1, t2 = float("inf"), float("inf")
            if 1 in dic:  # 可以删除一个模为 1 的最小数
                t1 = dic[1][0]
            if len(dic[2]) >= 2:  # 也可以删除模为 2 的最小的两个数
                t2 = dic[2][0] + dic[2][1]

            if t1 > t2:  # 选择两种可能中较小的值删除
                return s - t2

            return s - t1

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float("-inf"), float("-inf")]  # 不可达用 -inf
        for num in nums:
            prev = dp[:]
            for r in range(3):
                if prev[r] == float("-inf"):
                    continue
                nr = (r + num) % 3
                dp[nr] = max(dp[nr], prev[r] + num)
        return dp[0]


if __name__ == "__main__":
    # nums = [3,6,5,1,8]
    # nums = [4]
    # nums = [2,6,2,2,7]
    nums = [
        366,
        809,
        6,
        792,
        822,
        181,
        210,
        588,
        344,
        618,
        341,
        410,
        121,
        864,
        191,
        749,
        637,
        169,
        123,
        472,
        358,
        908,
        235,
        914,
        322,
        946,
        738,
        754,
        908,
        272,
        267,
        326,
        587,
        267,
        803,
        281,
        586,
        707,
        94,
        627,
        724,
        469,
        568,
        57,
        103,
        984,
        787,
        552,
        14,
        545,
        866,
        494,
        263,
        157,
        479,
        823,
        835,
        100,
        495,
        773,
        729,
        921,
        348,
        871,
        91,
        386,
        183,
        979,
        716,
        806,
        639,
        290,
        612,
        322,
        289,
        910,
        484,
        300,
        195,
        546,
        499,
        213,
        8,
        623,
        490,
        473,
        603,
        721,
        793,
        418,
        551,
        331,
        598,
        670,
        960,
        483,
        154,
        317,
        834,
        352,
    ]
    results = Solution().maxSumDivThree(nums)
    print(results)


# 3,6,
# nums = [5,1,8]
