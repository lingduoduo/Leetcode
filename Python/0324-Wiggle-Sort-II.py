class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if not nums: return None

        nums.sort()
        mid = (len(nums) - 1) // 2

        left = nums[mid::-1]
        right = nums[:mid:-1]

        for i in range(len(nums)):
            if i % 2 == 0 and left:
                nums[i] = left.pop(0)
            elif i % 2 == 1 and right:
                nums[i] = right.pop(0)
        return nums

        # mid = (len(nums)-1)//2
        # nums.sort()
        # nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]


if __name__ == "__main__":
    # nums = [5,1,1,6,2]
    nums = [1, 3, 2, 2, 3, 1]
    results = Solution().wiggleSort(nums)
    print(results)
