class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        res = 0

        reach = 0
        cur = 0
        i = 0
        while cur < n - 1:
            res += 1
            potential = cur
            while i <= potential:
                cur = max(cur, i + nums[i])
                i += 1
        return res

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    results = Solution().jump(nums)
    print(results)

