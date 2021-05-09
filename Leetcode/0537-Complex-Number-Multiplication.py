class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1, a2 = a.split("+")
        b1, b2 = b.split("+")
        
        res1 = int(a1) * int(b1) - int(a2[:-1]) * int(b2[:-1])
        res2 = int(a1) * int(b2[:-1]) + int(b1) * int(a2[:-1])
        return "+".join([f"{res1}", f"{res2}"+"i"])   


if __name__ == '__main__':
    a = "1+1i"
    b = "1+1i"
    res = Solution().complexNumberMultiply(a, b)
    print(res)

    a="1+-1i"
    b="1+-1i"
    res = Solution().complexNumberMultiply(a, b)
    print(res)