class Solution:
    def maximum69Number(self, num: int) -> int:
        if all([cha == "9" for cha in str(num)]):
            return num

        chas = [cha for cha in str(num)]
        i = 0
        while i < len(chas) and chas[i] == "9":
            i += 1
        chas[i] = "9"
        return int("".join(chas))
