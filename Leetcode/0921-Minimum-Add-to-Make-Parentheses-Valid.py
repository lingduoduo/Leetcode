class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = 0
        res = 0
        stack = []
        for s in S:
            if s == "(":
                stack.append(s)
                left += 1
            elif s == ")" and left > 0:
                stack.pop()
                left -= 1
            else:
                res += 1
        return res + len(stack)

if __name__ == '__main__':
    S = "())"
    res = Solution().minAddToMakeValid(S)
    print(res)

    S = "((("
    res = Solution().minAddToMakeValid(S)
    print(res)

    S = "()"
    res = Solution().minAddToMakeValid(S)
    print(res)

    S = "()))(("
    res = Solution().minAddToMakeValid(S)
    print(res)
        