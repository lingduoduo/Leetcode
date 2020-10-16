class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        res = 0

        reach = 0
        cur = 0
        pos = 0
        while cur < n - 1:
            res += 1
            potential = cur
            while pos <= potential:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return res

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    results = Solution().jump(nums)
    print(results)

