class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str=="": return 0
        i = 0
        
        if str[i]=="-": 
            flag=-1
            i+=1
        elif str[i]=="+":
            flag=1
            i+=1
        else:
            flag=1

        result=0
        while i<len(str):
            if str[i]<'0' or str[i]>'9': break 
            result=result*10+int(str[i])
            i+=1
        result=result*flag
        if result>2147483647: return 2147483647
        if result<-2147483647: return -2147483648
        return result