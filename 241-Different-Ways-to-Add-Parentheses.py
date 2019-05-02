class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        Example 1:
	        Input: "2-1-1"
			Output: [0, 2]
			Explanation: 
			((2-1)-1) = 0 
			(2-(1-1)) = 2
		Example 2:
			Input: "2*3-4*5"
			Output: [-34, -14, -10, -10, 10]
			Explanation: 
			(2*(3-(4*5))) = -34 
			((2*3)-(4*5)) = -14 
			((2*(3-4))*5) = -10 
			(2*((3-4)*5)) = -10 
			(((2*3)-4)*5) = 10		
        """
        res = list()

        for i in range(len(input)):
        	if input[i]=='+' or input[i]=='-' or input[i]=='*':
        		left = input[:i]
        		right = input[i+1:]

        		l = self.diffWaysToCompute(left)
        		r = self.diffWaysToCompute(right)

        		for num1 in l:
        			for num2 in r:
        				if input[i]=='+':
        					res.append(num1+num2)
        				elif input[i]=='-':
        					res.append(num1-num2)
        				elif input[i]=='*':
        					res.append(num1*num2)
        if not res:
        	res.append(int(input))
        return res
