# Method 1 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
	for k, v in enumerate(nums):
		i = k+1
		while i<len(nums):
			if v+nums[i] == target:
				return([k, i])
			else:
				i=i+1
	return([])

if __name__=="__main__":
	numbers=[2, 7, 11, 15]
	results = Solution().twoSum(numbers, 9)
	print(results)


class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for i,v in enumerate(nums):
            hash_map[v]=i

        for index1, v in enumerate(nums):
            if target-v in hash_map.keys():
                index2 = hash_map[target-v]
                return [index1+1, index2+1]

if __name__ == "__main__":
    numbers=[2,7,11,15]
    result = Solution().twoSum(numbers, 9)
    print result
    print 'Done'