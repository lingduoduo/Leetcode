class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      hash_set = set(nums)

      res = 0

      for num in nums:
        if num-1 not in hash_set:
            cnt = 0
            while num+cnt in hash_set:
                cnt += 1
            res = max(res, cnt)
      return res