from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for k in range(n - 2):
            i, j = k + 1, n - 1
            while i < j:
                cur_sum = nums[k] + nums[i] + nums[j]
                if cur_sum == 0:
                    res.add(tuple(sorted([nums[k], nums[i], nums[j]])))
                    i += 1
                    j -= 1
                elif cur_sum < 0:
                    i += 1
                else:
                    j -= 1
        return list(res)


if __name__ == "__main__":
    res = Solution().threeSum(nums=[0, 0, 0])
    print(res)
