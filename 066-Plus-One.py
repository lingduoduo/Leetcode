class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums=0
        for num in digits:
        	nums = nums*10+num

        nums+=1

        result=list(str(nums))
        result=[int(i) for i in result]
        return result
