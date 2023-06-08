class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        return max(res, cnt)


if __name__ == "__main__":
    res = Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1])
    print(res)
