from typing import List

class Solution(object):           
    def reverseWords(self, s: str, i: int) -> str:
        return s[-i:] + s[:-i]

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("abcdefg", 2))
