class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num is None:
        	return ""
        if num==0:
        	return "0"

        result = ""
        sign=""
        if num < 0:
        	sign = "-"
        	num = -num
        while num > 0:
        	result = str(num%7)+result
        	num = int(num/7)
        result = sign+result
        return result


if __name__=="__main__":
	s = -7
	result = Solution().convertToBase7(s)
	print(result)
