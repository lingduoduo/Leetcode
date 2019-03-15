# Method 1 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ## First Try
    	# for k, v in enumerate(nums):
    	# 	i = k+1
    	# 	while i<len(nums):
    	# 		if v+nums[i] == target:
    	# 			return([k, i])
    	# 		else:
    	# 			i=i+1

         #    hash_map = {}
         #    for i,v in enumerate(nums):
         #    hash_map[v]=i

         #    for index1, v in enumerate(nums):
         #        if target-v in hash_map.keys():
         #            index2 = hash_map[target-v]
         #    return [index1+1, index2+1]

        ## second try
        idx = dict()
        for i in range(len(nums)):
            idx[nums[i]] = i
        
        for i in range(len(nums)):
            if target-nums[i] in idx.keys() and i!=idx[target-nums[i]]:
                return([i, idx[target-nums[i]]])
        return None


if __name__ == "__main__":
    numbers=[3,2,4]
    result = Solution().twoSum(numbers, 6)
    print(result)
