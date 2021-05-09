class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = 0
        for w in word:
            if w.isupper():
                cap += 1

        if cap == len(word):
            return True
        elif cap == 0:
            return True
        elif cap == 1 and word[0].isupper():
            return True
        else:
            return False