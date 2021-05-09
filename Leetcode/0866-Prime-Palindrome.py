class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(x):
            if x == 1:
                return False
            for i in range(2,int(x**0.5)+1):
                if x%i == 0:
                    return False
            return True

        def isPalindrome(x):
            x = str(x)
            l = [ch for ch in x]
            return l[::-1]==l
           
        while True:
            if isPalindrome(N) and isPrime(N):
                break
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
        return N