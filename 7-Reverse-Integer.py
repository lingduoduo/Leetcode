class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x< -2**31 or x > 2**31-1:
            return 0
        ind = 1 if x > 0 else -1
        x = abs(x)
        result  = 0
        while x>0:
        	result = result*10 + x%10
        	x=x/10
        if result< -2**31 or result > 2**31-1:
            return 0
        return ind*result

if __name__=="__main__":
	numbers = 1534236469
	results = Solution().reverse(numbers)
	print(results)