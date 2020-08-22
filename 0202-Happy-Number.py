class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        result = n
        while result >= 0:
            l = list(str(result))
            result = 0
            
            while l:
                result += int(l.pop()) ** 2
            if result == 1 or result == 7:
                return True
            elif result < 10:
                return False


if __name__ == "__main__":
    n = 1111111
    result = Solution().isHappy(n)
    print(result)
