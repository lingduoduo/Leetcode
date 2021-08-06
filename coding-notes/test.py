import heapq

class Solution():
    def findGreatestSumOfSubArray(self, nums):
        if not nums:
            return 0
        curr = 0
        res = float("-inf")

        for i in range(len(nums)):
            curr += nums[i]
            if curr < 0:
                curr = 0 
            res = max(res, curr)

        return res

if __name__ == '__main__':
    res = Solution().findGreatestSumOfSubArray(nums=[1, -2, 3, 10, -4, 7, 2, -5])
    print(res)
