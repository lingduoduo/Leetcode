class Solution:
    def longestSubarray(self, nums, limit) -> int:
        max_stack = []
        min_stack = []
        left = 0
        ans = 0
        for right in range(len(nums)):
            while max_stack and nums[max_stack[-1]] < nums[right]:
                max_stack.pop()
            max_stack.append(right)
            while min_stack and nums[min_stack[-1]] > nums[right]:
                min_stack.pop()
            min_stack.append(right)
            while max_stack and min_stack and nums[max_stack[0]] - nums[min_stack[0]] > limit:
                if max_stack[0] <= left:
                    max_stack.pop(0)
                if min_stack[0] <= left:
                    min_stack.pop(0)
                left += 1
            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    nums = [1,2,3]
    limit = 4
    result = Solution().longestSubarray(nums, 4)
    print(result)
