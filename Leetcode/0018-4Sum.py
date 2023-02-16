from typing import List
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left + 1 < right and nums[left] == nums[left + 1]:
                            left+=1
                        left+=1
                        while left < right - 1 and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    result = Solution().fourSum(nums, 0)
    print(result)
