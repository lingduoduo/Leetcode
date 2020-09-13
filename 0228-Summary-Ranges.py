class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        res = []


        i = 0
        while i<len(nums):
            curr = [nums[i]]
            j = i+1
            while j<len(nums) and nums[j]==nums[j-1]+1:
                j += 1
            if j != i+1:
                curr.append(nums[j-1])
            i = j
            if len(curr) == 1:
                res.append(str(curr[0]))
            else:
                tmp = [str(num) for num in curr]
                res.append('->'.join(tmp))

        return res

if __name__=="__main__":
    nums = [0,1,2,4,5,7]
    result = Solution().summaryRanges(nums)
    print(result)

