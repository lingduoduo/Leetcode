class Solution:
    def replaceSpace(self, s):
    	strs = list(s)
    	for i in range(len(s)):
    		if s[i] == " ":
    			strs.append(" ")
    			strs.append(" ")

    	p1 = len(s) - 1
    	p2 = len(strs) - 1
    	while p1 >= 0 and p2 > p1:
    		print(strs)
    		if strs[p1] != " ":
    			strs[p2] = strs[p1]
    			p1 -= 1
    			p2 -= 1
    		else:
    			strs[p2] = "0"
    			p2 -= 1
    			strs[p2] = "2"
    			p2 -= 1
    			strs[p2] = "%"
    			p2 -= 1
    	return strs

if __name__ == '__main__':
    inputs = "A B"
    res = Solution().replaceSpace(inputs)
    print(res)
