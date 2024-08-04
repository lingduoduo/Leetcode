class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()

        res = []

        for idx, word in enumerate(words):
            if word[0] in "aeiouAEIOU":
                res.append(word + "maa" + "a" * idx)
            else:
                res.append(word[1:] + word[0] + "maa" + "a" * idx)
        return " ".join(res)
