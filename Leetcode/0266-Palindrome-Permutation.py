import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = collections.Counter(s)
        cnt = 0
        for k, v in d.items():
            if v % 2 == 0:
                cnt += 1
        return len(d.keys()) == cnt or len(d.keys()) == cnt + 1

if __name__ == "__main__":
    res = Solution().canPermutePalindrome(s = "codde")
    print(res)

    res = Solution().canPermutePalindrome(s = "aab")
    print(res)