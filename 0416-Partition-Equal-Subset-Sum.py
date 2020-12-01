# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
        
#         n = len(nums)
#         s = sum(nums)
        
#         if s % 2 != 0:
#             return False
        
#         dp = [0] * (s + 1)
#         dp[0] = 1
#         for num in nums:
#             for i in range(s, -1, -1):
#                 if dp[i]:
#                     dp[i+num] = 1
                    
#             if dp[s//2]:
#                 return True
            
#         return False


class Solution(object):
    def canPartition(self, nums) -> bool:
        n = len(nums)
        tot = len(nums)
        res = []
        for i in range(1<<n):
            tmp = []
            for j in range(n):
                if j & i == 1:
                    tmp.join(nums[i])
            res.append(tmp)
        print(tmp)


if __name__ == '__main__':
    nums = [1,5,11,5]
    res = olution().canPartition(nums)
    print(res)
            