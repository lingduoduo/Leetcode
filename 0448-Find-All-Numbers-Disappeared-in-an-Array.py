class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # m = len(nums)
        # nums_set = set(nums)
        # res = []
        
        # for num in range(1, m+1):
        #     if num not in nums_set:
        #         res.append(num)
        # return res
        
        # res = set(i for i in range(1, len(nums)+1))
        # return list(res - set(nums))
        
        res = [i for i in range(1, len(nums) + 1)]
        
        for num in nums:
            res[num - 1] = 0
        
        return [i for i in res if i > 0]


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = Solution().findDisappearedNumbers(nums)
    print(result)
    
