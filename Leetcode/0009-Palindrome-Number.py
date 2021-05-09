class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        ####First try
        ###if x<0 or (x%10 == 0 and x!=0): 
        ###    return False
        ###if x in range(10):
        ###    return True

        ###revx = 0
        ###i = x

        ###while i>0:
        ###    revx = revx*10 + i%10
        ###    i=int(i/10)

        ###if revx == x:
        ###    return True
        ###else:
        ###    return False

        ####Second try
        ###if x<0:
        ###    return False
        ###else:
        ###    num = str(x)
        ###    return num[::-1]==num
        
        ###third try
        input = x
        if x < 0:
            return False
        res = 0
        while x>0:
            res = res*10 + x%10
            x = x//10
        if res == input:
            return True
        else:
            return False

if __name__=="__main__":
    results = Solution().isPalindrome(88888)
    print(results)
    results = Solution().isPalindrome(10)
    print(results)

