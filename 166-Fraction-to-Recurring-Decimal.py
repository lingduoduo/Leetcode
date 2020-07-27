class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
i        negative_flag = numerator * denominator < 0
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        numlist = []
        cnt = 0
        loopDict = dict()
        loopStr = None
        
        while True:
            numlist.append(str(numerator//denominator))
            cnt += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loc = loopDict.get(numerator)
            if loc:
                loopStr = "".join(numlist[loc:cnt])
                break
            
            loopDict[numerator] = cnt
        
        res = numlist[0]
        
        if len(numlist) > 1:
            res += '.'
        
        if loopStr:
            res += "".join(numlist[1:len(numlist)-len(loopStr)])+"("+loopStr+")"
        else:
            res += "".join(numlist[1:])
        
        if negative_flag:
            return "-" + res
        else:
            return res