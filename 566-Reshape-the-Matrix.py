class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        m = len(nums[0])
        if n==0 and m==0:
        	return nums
        if n*m != r*c:
        	return nums
        results = [ [0]*c for _ in range(r)]
        for i in range(n*m):
        	nums_i = int(i/m)
        	nums_j = int(i%m)
        	results_r = int(i/c)
        	results_c = int(i%c)
        	results[results_r][results_c] = nums[nums_i][nums_j] 
        return results

if __name__== "__main__":
	print(Solution().matrixReshape([[1,2],[3,4]], 4, 1))

