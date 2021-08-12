from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        for word in words:
            res += word 
            if res == s:
                return True
        return False

if __name__ == '__main__':
    res = Solution().isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"])
    print(res)