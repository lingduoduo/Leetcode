class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        if not nums or nums[0]>0 or nums[len(nums)-1]<0: return []
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[j]+nums[k] < target:
                    j+=1
                else:
                    k-=1
        return res

if __name__=="__main__":
    # nums=[-1, 0, 1, 2, -1, -4]
    # nums=[3,0,-2,-1,1,2]
    nums=[0,0,0,0]
    result = Solution().threeSum(nums)
    print(result)
