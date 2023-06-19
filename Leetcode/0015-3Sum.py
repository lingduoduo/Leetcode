from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return list(res)


if __name__ == "__main__":
    # res = Solution().threeSum(nums=[0, 0, 0])
    # print(res)

    res = Solution().threeSum([-2, 0, 1, 1, 2])
    print(res)
