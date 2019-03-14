class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
        	return False
        if n==1:
            return True

        cnt = 0
        cur = n
        while cur>0:
        	cur=cur//3
        	cnt+=1

        return 3**(cnt-1) == n

if __name__ == "__main__":
	input = 9
	result = Solution().isPowerOfThree(input)
	print(result)   