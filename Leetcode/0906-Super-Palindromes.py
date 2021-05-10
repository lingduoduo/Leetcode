class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        upper = 10**5
        res = 0

        for i in range(upper):
            s = str(i)
            t = int(s + s[-2::-1]) ** 2
            if t > right:
                break
            if t >= left and str(t) == str(t)[::-1]:
                res += 1

        for i in range(upper):
            s = str(i)
            t = int(s + s[::-1]) ** 2
            if t > right:
                break
            if t >= left and str(t) == str(t)[::-1]:
                res += 1
        return res   
