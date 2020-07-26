class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = s.strip()
        # p = re.compile(r'\s{2,}')
        # s = p.sub(" ", s)
        # words = s.split(" ")
        # return " ".join(words[::-1])
        
        if s == "":
            return s
        
        s = s.strip()
        ls = s.split(" ")
        if ls == []:
            return ""
        
        res = ""
        for i in range(len(ls)-1):
            if ls[len(ls)-1-i] != "":
                res += ls[len(ls)-1-i] + " "
        res += ls[0]
        
        return res
    
if __name__ == "__main__":
    s = "   the sky is blue   "
    result = Solution().reverseWords(s)
    print(result)