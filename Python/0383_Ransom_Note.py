import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_ransom = collections.Counter(ransomNote)
        d_magazine = collections.Counter(magazine)
        return d_ransom & d_magazine == d_ransom


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for cha in ransomNote:
            if cha not in d:
                return False
            d[cha] -= 1
            if d[cha] == 0:
                del d[cha]
        return True


if __name__ == "__main__":
    res = Solution().canConstruct(ransomNote="aa", magazine="ab")
    print(res)
