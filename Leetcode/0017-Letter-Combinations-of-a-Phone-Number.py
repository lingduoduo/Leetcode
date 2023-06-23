from typing import List


class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
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


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
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

        res = []

        def dfs(idx, path):
            nonlocal res
            if path == len(digits):
                res.append(''.join(path))

            if idx >= len(digits):
                return

            for cha in d[digits[idx]]:
                path.append(cha)
                dfs(idx + 1, path)

        dfs(0, [])
        return res


if __name__ == "__main__":
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)
