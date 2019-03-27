class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=list(s)
        pos=[]
        l2=[]
        for i in range(len(l1)):
        	if l1[i] in ['i','e','a','o','u', 'A', 'E', 'I', 'O', 'U']:
        		pos.append(i)
        		l2.append(l1[i])
        l2=l2[::-1]
        for i in range(len(l2)):
        	l1[pos[i]]=l2[i]
        return ''.join(l1)

if __name__=="__main__":
    # s="hello"
    # result = Solution().reverseVowels(s)
    # print(result)      
    s="aA"
    result = Solution().reverseVowels(s)
    print(result)  

