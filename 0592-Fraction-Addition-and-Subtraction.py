class Solution:
    def fractionAddition(self, expression: str) -> str:
        # re can split string with multiple delimeter
        # import re
        # nums = re.split('[+-]', expression)
        s = '+' + expression if expression[0] != '-' else expression
        sign = [i for i in range(len(s)) if s[i] in ('+', '-')]
        sign.append(len(s))
        
        numerator, denominator = [], []
        for i in range(len(sign) - 1):
            n, d = s[sign[i] + 1:sign[i+1]].split('/')
            flag = -1 if s[sign[i]] == '-' else 1
            numerator.append(int(n) * flag)
            denominator.append(int(d))
        
        def gcd(n1, n2):
            if n1 < n2:
                n1, n2 = n2, n1
            while n2 != 0:
                n1, n2 = n2, n1 % n2
            return n1
            
        lcm = reduce(lambda a,b: a*b//gcd(a,b), denominator)
        numerator_sum = 0
        for i in range(len(numerator)):
            numerator_sum += numerator[i] * (lcm // denominator[i])
        # gcd for numerator and denominator
        commom = gcd(abs(numerator_sum), lcm)
        return str(numerator_sum//commom) + '/' + str(lcm//commom)
           	