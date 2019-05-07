class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def isSelfDividing(number):
            if '0' in str(number):
                return False
            curr = number
            while curr > 0:
                d = curr % 10
                if number % d != 0:
                    return False
                curr = curr // 10
            return True
        
        result = list()
        for num in range(left, right + 1):
            if isSelfDividing(num):
                result.append(num)
        return result
