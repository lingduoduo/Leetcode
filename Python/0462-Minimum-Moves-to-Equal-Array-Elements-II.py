class Solution:
    def minMoves2(self, nums) -> int:
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        steps = sum([abs(num - mid) for num in nums])
        return steps


if __name__ == "__main__":
    nums = [1, 2, 3]
    res = Solution().minMoves2(nums)
    print(res)

    nums = [1, 5, 6]
    res = Solution().minMoves2(nums)
    print(res)
