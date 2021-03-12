from typing import List
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
    	# Count # of sub arrays whose max element is <= N
    	def countarray(nums, bound):
    		res = 0
    		cur = 0
    		for num in nums:
    			if num <= bound:
    				cur += 1
    				res += cur
    			else:
    				cur = 0
    		return res

    	return countarray(A, R) - countarray(A, L - 1)

if __name__ == '__main__':
	A = [2, 1, 4, 3]
	L = 2
	R = 3
	res = Solution().numSubarrayBoundedMax(A, L, R)
	print(res)