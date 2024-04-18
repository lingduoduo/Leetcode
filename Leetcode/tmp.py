from typing import List
import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        return r & m 



if __name__ == "__main__":
    res = Solution().canConstruct(ransomNote = "aab", magazine = "aa")
    print(res)