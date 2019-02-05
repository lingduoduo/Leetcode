class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividing(number):
        	curr = number
        	while curr>0:
        		d = curr%10
        		if number%d != 0:
        			return False
        		curr = curr // 10
        	return True

        result = list()
        for num in range(left, right):
        	if isSelfDividing(num):
        		result.append(num)
        return result