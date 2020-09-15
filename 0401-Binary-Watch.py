class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return "0:00"

        res = []    

        i = num
        
        while i<60:
            if i<11:
                res.append(str(i)+":00")
            if i<10:
                res.append("0:0"+str(i))
            else:
                res.append("0:"+str(i))
            i *= 2
        return res

