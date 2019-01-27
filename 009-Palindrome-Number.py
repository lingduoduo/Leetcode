class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x!=0): 
            return False
        if x in range(10):
            return True

        revx = 0
        i = x

        while i>0:
            revx = revx*10 + i%10
            i=int(i/10)

        if revx == x:
            return True
        else:
            return False

if __name__=="__main__":
	numbers = 88888
	results = Solution().isPalindrome(numbers)
	print(results)


    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     if x<0: 
    #         return False
    #     strX = str(x)
    #     if strX == strX[::-1]:
    #         return True
    #     else:
    #         return False
