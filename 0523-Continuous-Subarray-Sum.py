import collections
class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        dp = collections.defaultdict()
        dp[0] = -1
        tot = 0
        m = -1
        for i, num in enumerate(nums):
            print(dp)
            tot += num
            if k==0: 
                m = tot
            else: 
                m = tot % k
            if dp.get(m)==None: 
                dp[m] = i
            elif i - dp[m] > 1: 
                return True
        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k=6
    results = Solution().checkSubarraySum(nums, k)
    print(results)
