class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ###first try
        ###if digits == "":
        ###    return []
        #
        ###self.d = dict()
        ###self.d['0'] = ''
        ###self.d['1'] = ''
        ###self.d['2'] = 'abc'
        ###self.d['3'] = 'def'
        ###self.d['4'] = 'ghi'
        ###self.d['5'] = 'jkl'
        ###self.d['6'] = 'mno'
        ###self.d['7'] = 'pqrs'
        ###self.d['8'] = 'tuv'
        ###self.d['9'] = 'wxyz'
        #
        ###self.result = []
        ###self.dfs(0, '', digits)
        ###return self.result
        #
        ###def dfs(self, num, path, digits):
        ###    if num == len(digits):
        ###        self.result.append(path)
        ###        return
        ###    for letter in self.d[digits[num]]:
        ###        self.dfs(num + 1, path + letter, digits)

        ###second try
        ###import itertools
        #
        ###res = self.d[digits[0]]
        ###for i in range(1, len(digits)):
        ###    new_res = []
        ###    for x, y in itertools.product(res, self.d[digits[i]]):
        ###        new_res.append(x + y)
        ###    res = new_res
        #
        ###return res

        if digits == "":
            return []

        d = dict()
        d[0] = "0"
        d[1] = "1"
        d[2] = "abc"
        d[3] = "def"
        d[4] = "ghi"
        d[5] = "jkl"
        d[6] = "mno"
        d[7] = "pqrs"
        d[8] = "tuv"
        d[9] = "wxyz"

        res = [""]
        if not digits:
            return res

        for digit in digits:
            tmp = []
            for ch in d[int(digit)]:
                for str in res:
                    tmp.append(str + ch)
            res = tmp
        return res


if __name__ == "__main__":
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)
