class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 2:
            return nums[0]

        answers = 0
        for i in range(0, len(nums), 2):
            answers += nums[i]
        return answers


if __name__ == "__main__":
    print(Solution().arrayPairSum([1, 2, 6, 7]))
