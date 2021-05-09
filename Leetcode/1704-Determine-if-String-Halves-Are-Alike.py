class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        f = [1 for cha in s[:len(s)//2] if cha in 'aeiou']
        l = [1 for cha in s[len(s)//2:] if cha in 'aeiou']
        return f == l

if __name__ == '__main__':
    s = "MerryChristmas"
    res = Solution().halvesAreAlike(s)
    print(res)