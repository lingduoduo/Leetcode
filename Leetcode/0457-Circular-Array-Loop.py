class Solution:
    def circularArrayLoop(self, nums) -> bool:
        for start in range(len(nums)):
            slow = start
            fast = (start + nums[start]) % len(nums)
            while (nums[slow] * nums[fast] > 0) and (nums[slow] * nums[(fast + nums[fast]) % len(nums)]) > 0:
                if fast == slow:
                    if slow == (slow + nums[slow]) % len(nums):
                        break
                    return True
                slow = (slow + nums[slow]) % len(nums)
                fast = (fast + nums[fast]) % len(nums)
                fast = (fast + nums[fast]) % len(nums)
        return False

if __name__ == '__main__':
    # nums = [-2,1,-1,-2,-2]
    # res = Solution().circularArrayLoop(nums)
    # print(res)

    # nums = [-1,2]
    # res = Solution().circularArrayLoop(nums)
    # print(res)

    # nums = [2,-1,1,2,2]
    # res = Solution().circularArrayLoop(nums)
    # print(res)  

    # nums = [-1,-2,-3,-4,-5]
    # res = Solution().circularArrayLoop(nums)
    # print(res)  

    # nums = [1,1]
    # res = Solution().circularArrayLoop(nums)
    # print(res)

    nums = [-2,1,-1,-2,-2]
    res = Solution().circularArrayLoop(nums)
    print(res)