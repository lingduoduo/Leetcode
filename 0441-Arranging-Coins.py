class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        tot = 0

        while tot + i < n:
            tot += i
            i += 1
        if n - tot == i:
            return i
        else:
            return i-1
