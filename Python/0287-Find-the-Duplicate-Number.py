from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                else:
                    j = nums[i] - 1
                    nums[i], nums[j] = nums[j], nums[i]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l <= r:
            mid = l + (r - l) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    res = Solution().findDuplicate(nums=[1, 3, 4, 2, 2])
    print(res)
