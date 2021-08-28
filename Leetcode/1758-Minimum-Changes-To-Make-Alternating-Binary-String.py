class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)//2
        strs = "01" * n
        res1 = [1 if strs[i] == s[i] else 0 for i in range() ]
        print(res1)
        strs = "10" * n
        res2 = [1 if strs[i] == s[i] else 0 for i in range(n) if strs[i] == s[i] ]
        print(res2)
        # return len(s) - max(res1, res2)

if __name__ == '__main__':
    res = Solution().minOperations(s = "0100")
    print(res)
    