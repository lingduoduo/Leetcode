class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 0
        curr = 0
        for i in range(1, len(nums)):
        	if nums[curr] != nums[i]:
        		times = 0
        		curr += 1
        		nums[curr] = nums[i]
        	elif nums[curr] == nums[i] and times == 0:
        		times += 1
        		curr += 1
        		nums[curr] = nums[i]

        return nums[:curr]

if __name__ == "__main__":
    numbers = [1,1,1,2,2,3]
    numbers = [0,0,1,1,1,1,2,3,3]
    result = Solution().removeDuplicates(numbers)
    print(result)
