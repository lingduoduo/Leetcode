class Solution:
    def thousandSeparator(self, n: int) -> str:
        word = str(n)[::-1]
        i = 1
        res = []
        for cha in word:
            res.append(cha)
            if i % 3 == 0 and i != len(word):
                res.append(".")
            i += 1
        return ''.join(res[::-1])
            