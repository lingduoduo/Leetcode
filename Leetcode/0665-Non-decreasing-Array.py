class Solution:
    def checkPossibility(self, nums) -> bool:
        isIncrease = lambda nums: all(
            nums[i] <= nums[i + 1] for i in range(len(nums) - 1)
        )
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = one[i + 1]
                two[i + 1] = two[i]
                break
        return isIncrease(one) or isIncrease(two)


if __name__ == "__main__":
    # nums = [4,2,3]
    # nums = [4,2,1]
    nums = [3, 4, 2, 3]
    results = Solution().checkPossibility(nums)
    print(results)
