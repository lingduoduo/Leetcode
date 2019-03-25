class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        d = dict()
        for i in range((len(nums))-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] in d:
                    d[nums[i]+nums[j]].append([i,j])
                else:
                    d[nums[i]+nums[j]]=[[i,j]]
        res =[]
        for i in d:
            if target-i in d:
                list1=d[i]
                list2=d[target-i]
                for k1 in range(len(list1)):
                    for k2 in range(len(list2)):
                        item = [nums[list1[k1][0]], nums[list1[k1][1]], nums[list2[k2][0]], nums[list2[k2][1]]]
                        item = sorted(item)
                        if (list1[k1][0] not in list2[k2]) and (list1[k1][1] not in list2[k2]) and item not in res:
                            res.append(item)
        return res
        
if __name__=="__main__":
    nums=[1, 0, -1, 0, -2, 2]
    result = Solution().fourSum(nums, 0)
    print(result)
