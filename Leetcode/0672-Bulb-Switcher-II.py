class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if m == 0:
            return 1
        if n >= 3:
            return 4 if m == 1 else 7 if m == 2 else 8
        if n == 2:
            return 3 if m == 1 else 4
        if n == 1:
            return 2
