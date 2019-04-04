class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        
        self.d = dict()
        self.d['0'] = ''
        self.d['1'] = ''
        self.d['2'] = 'abc'
        self.d['3'] = 'def'
        self.d['4'] = 'ghi'
        self.d['5'] = 'jkl'
        self.d['6'] = 'mno'
        self.d['7'] = 'pqrs'
        self.d['8'] = 'tuv'
        self.d['9'] = 'wxyz'

        self.result = []
        self.dfs(0, '', digits)
        return self.result


    def dfs(self, num, path, digits):
        if num == len(digits):
            self.result.append(path)
            return
        for letter in self.d[digits[num]]:
            self.dfs(num+1, path+letter, digits)

if __name__ == "__main__":
    digits = '23'
    result = Solution().letterCombinations(digits)
    print(result)