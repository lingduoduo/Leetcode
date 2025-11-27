from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return False


if __name__ == "__main__":
    res = Solution().search(
        nums=[
            -9,
            -8,
            -8,
            -8,
            -8,
            -7,
            -7,
            -7,
            -7,
            -7,
            -7,
            -6,
            -6,
            -6,
            -6,
            -6,
            -5,
            -5,
            -4,
            -4,
            -4,
            -4,
            -4,
            -4,
            -4,
            -3,
            -3,
            -3,
            -3,
            -3,
            -2,
            -1,
            -1,
            -1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            5,
            5,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            8,
            8,
            8,
            9,
            9,
            9,
            9,
            10,
            10,
            10,
            10,
            -10,
            -10,
            -10,
            -10,
            -10,
            -10,
            -9,
            -9,
            -9,
        ],
        target=13,
    )
    print(res)
