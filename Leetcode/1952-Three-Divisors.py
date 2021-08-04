import math
class Solution:
    def isThree(self, n: int) -> bool:
        if n == 4:
            return True
        elif n < 4:
            return False
        elif n % 2 == 0:
            return False
        else:
            m = int(math.sqrt(n))
            if m * m < n:
                return False
            else:
                for i in range(2, m):
                    if n % i == 0:
                        return False
                return True    
                
if __name__ == '__main__':
    res = Solution().isThree(n=121)
    print(res)