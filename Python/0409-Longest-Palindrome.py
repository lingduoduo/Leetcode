import collections


class Solution(object):
    def longestPalindrome(self, s):
        chars = [c for c in s]
        d = collections.Counter(chars)
        res = 0
        flag = 0
        print(d)
        for k, v in d.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                flag = 1
        return res + flag


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        print(ss)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)


if __name__ == "__main__":
    numbers = "abccccdd"
    ###numbers = "ccc"
    # numbers = "bananas"
    result = Solution().longestPalindrome(numbers)
    # print(result)
    print("Done")
