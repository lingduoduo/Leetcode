class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        s = list()

        for op in ops:
        	if op =="+":
        		num1 = s.pop()
        		num2 = s.pop()
        		s.appen(num1+num2)
        	elif op =="C":
        		s.pop()
        	elif op =="D":
        		num1 = s.pop()
        		s.appen(num1*2)
        	else:
        		s.append(int(op))
        return sum(s)
 