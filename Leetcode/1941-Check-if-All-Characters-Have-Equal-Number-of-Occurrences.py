import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """Input: s = "abacbc"
        Output: true
        Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
        """
        cnt = collections.Counter(s)
        tmp = cnt.values()
        return len(set(tmp)) == 1


if __name__ == "__main__":
    res = Solution().areOccurrencesEqual(s="abacbc")
    print(res)
