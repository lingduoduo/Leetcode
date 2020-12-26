class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return getscore(0, len(nums)-1)

        def getscore(left, right):
            if left == right:
                return nums[left]

            return max(nums[left] - getscore(nums, left+1, right), nums[right] - getscore(nums, right-1))