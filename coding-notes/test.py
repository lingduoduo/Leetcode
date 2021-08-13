class Solution:
    def multiply(self, nums) -> int:
        res = [1] * len(nums)
        prod = 1
        for i in range(1, len(nums)):
            prod *=  nums[i - 1]
            res[i] = prod

        prod = 1
        for i in reversed(range(len(nums) - 1)):
            prod *=  nums[i + 1]
            res[i] *= prod

        return res

        
if __name__ == '__main__':
    res = Solution().multiply(nums = [1,2,3,4,5])
    print(res)

