class Solution:
    def minMoves(self, nums):
        res = 0

        while not all(num == nums[0] for num in nums):
            print(nums)
            nums.sort()
            nums[0] += 1
            nums[1] += 1
            res += 1
        return res


class Solution:
    def minMoves(self, nums):
        nums.sort()
        res = 0
        for num in nums:
            res += num - nums[0]
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    results = Solution().minMoves(nums)
    print(results)
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
