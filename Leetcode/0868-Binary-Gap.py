class Solution:
    def binaryGap(self, n: int) -> int:
        nums = []
        i = 0
        while n > 0:
            if n % 2 == 1:
                nums.append(i)
            n = n // 2
            i += 1
        print(nums)
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i]-nums[i-1])
        return res

if __name__ == '__main__':
    res = Solution().binaryGap(22)
    print(res)
