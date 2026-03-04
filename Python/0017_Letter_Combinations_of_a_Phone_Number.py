from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        d = dict()
        d["0"] = ""
        d["1"] = ""
        d["2"] = "abc"
        d["3"] = "def"
        d["4"] = "ghi"
        d["5"] = "jkl"
        d["6"] = "mno"
        d["7"] = "pqrs"
        d["8"] = "tuv"
        d["9"] = "wxyz"

        res = []
        def dfs(idx, path):
            nonlocal res
            if path == len(digits):
                res.append("".join(path))
            if idx >= len(digits):
                return
            for cha in d[digits[idx]]:
                path.append(cha)
                dfs(idx + 1, path)
        dfs(0, [])
        return res


class Solution:
    def letterCombinations(digits):
        letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz",  # 9
        ]

        def getCombinations(self, digits, index, s):
            if index == len(digits):
                result.append(s)
                return
            digit = int(digits[index])
            letters = letterMap[digit]
            for letter in letters:
                self.getCombinations(digits, index + 1, s + letter)

        result = []
        if len(digits) == 0:
            return result

        getCombinations(digits, 0, "")
        return result


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return None
            
        letterMap = [
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

        res = [""]
        for digit in digits: #"23"
            cur = []
            for pre in res:
                for ch in letterMap[ord(digit) - ord("2")]:
                    cur.append(pre + ch)
            res = cur[:]
        return res

if __name__ == "__main__":
    digits = "23"
    result = Solution().letterCombinations(digits)
    print(result)
