class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        
        d = dict()
        d['0'] = ''
        d['1'] = ''
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        
        result = []

        def dfs(num, path):
            if num == len(digits):
                result.append(path)
                return
            for letter in d[digits[num]]:
            	dfs(num+1, path+letter)

        dfs(0, '')
        return result