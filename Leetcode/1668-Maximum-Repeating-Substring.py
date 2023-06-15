import re


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        nextstr = word
        while sequence.find(nextstr) >= 0:
            res += 1
            nextstr = word * (res + 1)
        return res


if __name__ == "__main__":
    # sequence = "ababc"
    # word = "ab"
    # res = Solution().maxRepeating(sequence, word)
    # print(res)

    # sequence = "ababc"
    # word = "ba"
    # res = Solution().maxRepeating(sequence, word)
    # print(res)

    # sequence = "ababc"
    # word = "ac"
    # res = Solution().maxRepeating(sequence, word)
    # print(res)

    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaabaaaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    res = Solution().maxRepeating(sequence, word)
    print(res)
