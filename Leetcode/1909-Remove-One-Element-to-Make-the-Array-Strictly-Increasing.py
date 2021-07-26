class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            tmp = nums[:i] + nums[i+1:]

            j = 0
            while j < len(tmp)-1 and tmp[j] < tmp[j+1]:
                j += 1
            if j == len(tmp) - 1:
                return True
            
        return False

if __name__ == '__main__':
    res = Solution().canBeIncreasing(nums=[1,1,1])
    print(res)