class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B=="":
            return True
        for i in range(len(A)):
            if A[i+1:]+A[:i+1]==B:
                return True
        return False

if __name__=="__main__":
    A = 'abcde'
    B = 'cdeab'
    result = Solution().rotateString(A, B)
    print(result)       

    A = 'abcde'
    B = 'abced'
    result = Solution().rotateString(A, B)
    print(result)      