class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_ransom = collections.Counter(ransomNote)
        d_magazine = collections.Counter(magazine)

        for k, v in d_ransom:
            if d_magazine[k] < v:
                return False
        return True
