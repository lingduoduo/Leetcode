import collections
class Solution(object):
    def isContinuous(self, nums):
        nums.sort()

        cnt = sum([1 for num in nums if num == 0])
        
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]: 
                return False
            else:
                cnt -= nums[i + 1] - nums[i] - 1 
        return cnt >= 0


if __name__ == '__main__':
    res = Solution().isContinuous(nums=[1, 0, 3, 4, 5])
    print(res)

    res = Solution().isContinuous(nums=[1, 2, 4, 6, 7])
    print(res)
