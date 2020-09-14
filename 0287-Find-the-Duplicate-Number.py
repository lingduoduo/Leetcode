class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left <= right:
            mid = left + (right-left)//2
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    cnt += 1
            if cnt<=mid:
                left = mid + 1
            else:
                right = mid-1
        return left


