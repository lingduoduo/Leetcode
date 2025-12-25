from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:        
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if abs(tot - target) < abs(res - target):
                    res = tot
                if tot == target:
                    return tot
                elif tot < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res



if __name__ == "__main__":
    nums = [0, 1, 2]
    # nums = [-1,-5,-3,-4,2,-2]
    # nums = [0, 2, 1, -3]
    result = Solution().threeSumClosest(nums, 3)
    print(result)
