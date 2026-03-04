from typing import List

def letterCombinations(digits):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(path, idx):
        if idx == len(digits):
            res.append(path)
            return
        
        for letter in phone[digits[idx]]:
            backtrack(path + letter, idx + 1)

    res = []
    if digits:
        backtrack("", 0)
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
