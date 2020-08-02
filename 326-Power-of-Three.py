class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if not n:
        #     return False
        # if n < 3:
        #     return False
        #
        # cnt = 0
        # cur = n
        # while cur > 0:
        #     cur = cur // 3
        #     cnt += 1
        #
        # return 3 ** (cnt - 1) == n
        
        if n <= 1:
            return True
        elif n <= 2:
            return False
        
        while n > 3:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        
        if n == 3:
            return True
        else:
            return False
            
        
        


if __name__ == "__main__":
    input = 9
    result = Solution().isPowerOfThree(input)
    print(result)
