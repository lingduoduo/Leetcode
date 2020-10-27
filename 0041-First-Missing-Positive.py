class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        min_num = 1
        max_num = max(nums)
        for i in range(min_num, max_num+2):
            if i not in nums:
                return i
        return min_num
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        l = len(nums)
        if l == 1:
            return 1
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0
        for i in range(l):
            nums[nums[i] % l] += l
        for i in range(1, l):
            if nums[i] < l:
                return i
        return l