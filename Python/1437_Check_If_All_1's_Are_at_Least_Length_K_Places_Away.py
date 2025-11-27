class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        for idx, num in enumerate(nums):
            if num == 1 and prev > -1:
                if idx - prev - 1 < k:
                    return False
            if num == 1:
                prev = idx
        return True
