class Solution:
    def totalHammingDistance(self, nums) -> int:
        res = 0
        mask = 1
        n = len(nums)
        for i in range(32):
            cnt = 0
            for num in nums:
                if num & mask:
                    cnt += 1
            res += cnt *  (n - cnt)
            mask <<= 1
        return res

if __name__ == '__main__':
    nums = [4, 14, 2]
    res = Solution().totalHammingDistance(nums)
    print(res)