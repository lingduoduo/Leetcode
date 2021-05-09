class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        i = 0
        maxstep = nums[0]
        while i <= maxstep:
            print([i, maxstep])
            if maxstep >= len(nums) - 1:
                return True
            maxstep = max(maxstep, nums[i] + i)
            i += 1
        return False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    result = Solution().canJump(nums)
    print(result)

    nums = [3, 2, 1, 0, 4]
    result = Solution().canJump(nums)
    print(result)
