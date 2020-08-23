class Solution:
    def findWords(self, words: List[str]) -> List[str]:
    	rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3

        res = []
        for word in words:
        	for i in range(len(word)):
        		if i == 0:
        			curr = rowdict[word[i]]
        		else:
        			if curr != rowdict[word[i]]:
        				break
        	if i == len(word):
        		res.append(word)
        return res
