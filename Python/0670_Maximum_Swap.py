class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        left = 0
        right = 0

        max_idx = len(nums) - 1

        for idx in reversed(range(len(nums))):
            if nums[idx] > nums[max_idx]:
                max_idx = idx
            elif nums[idx] < nums[max_idx]:
                left = idx
                right = max_idx
        nums[left], nums[right] = nums[right], nums[left]
        return int("".join(nums))

class Solution:
    def maximumSwap(self, num: int) -> int:
        strs = list(str(num))
        last = [-1] * 10

        for i, v in enumerate(strs):
            last[ord(v) - ord('0')] = i
        
        for i, ch in enumerate(strs):
            cur = ord(ch) - ord('0')
            for d in range(9, cur, -1):
                if last[d] > i:
                    j = last[d]
                    strs[i], strs[j] = strs[j], strs[i]
                    return int("".join(strs))
        return num