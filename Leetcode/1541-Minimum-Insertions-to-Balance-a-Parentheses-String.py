
class Solution:
    def minInsertions(self, s: str) -> int:
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res

if __name__ == '__main__':
    res = Solution().minInsertions(s = "))())(")
    print(res)


