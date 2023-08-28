class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        a = bin(k+1)
        b = a[3:]
        number = b.replace("0","4").replace("1","7")
        return number