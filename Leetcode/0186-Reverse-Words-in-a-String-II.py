from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(s, start, i - 1)
                start = i + 1
            elif i == len(s) - 1:
                self.reverse(s, start, i)

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1


if __name__ == "__main__":
    res = Solution().reverseWords(s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
    print(res)
