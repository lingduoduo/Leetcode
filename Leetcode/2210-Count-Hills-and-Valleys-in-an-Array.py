from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        stack = [nums[0]]
        for i in range(1, len(nums)):
            print(stack)
            if nums[i] == stack[-1]:
                continue
            if len(stack) < 2:
                stack.append(nums[i])
                continue
            if stack[-2] < stack[-1] and stack[-1] > nums[i]:
                res += 1
            elif stack[-2] > stack[-1] and stack[-1] < nums[i]:
                res += 1
            stack.append(nums[i])
        return res

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hillValley = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:     #hill check
                hillValley += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:     #valley check
                hillValley += 1
        return hillValley

if __name__ == "__main__":
    res = Solution().countHillValley(nums=[2, 4, 1, 1, 6, 5])
    print(res)

    res = Solution().countHillValley(nums=[6, 6, 5, 5, 4, 1])
    print(res)
