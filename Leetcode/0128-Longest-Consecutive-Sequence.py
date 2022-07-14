class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in hash_set:
                cnt = 0
                while num + cnt in hash_set:
                    cnt += 1
                res = max(res, cnt)
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            current_length = 1
            cur = nums[i]
            while (cur + 1 in nums_set):
                current_length += 1
                cur += 1
            res = max(res, current_length)
        return res
