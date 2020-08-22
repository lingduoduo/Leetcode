class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## return n/5 + n/25 + n/125 + ...
        # result = 0
        # i = 1
        # while n / 5 ** i > 0:
        #     result += n / 5 ** i
        #     i += 1
        # return result
        
        res = 0
        
        while n != 0:
            res += n//5
            n = n//5
        return res
        


if __name__ == "__main__":
    numbers = 5
    results = Solution().trailingZeroes(numbers)
    print(results)
