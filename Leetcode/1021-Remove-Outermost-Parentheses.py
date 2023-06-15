class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = []
        for s in S:
            if s == "(":
                stack.append(s)
                if len(stack) >= 2:
                    res.append(s)
            elif s == ")":
                if len(stack) >= 2:
                    stack.pop()
                    res.append(s)
                else:
                    stack.pop()
        return "".join(res)


if __name__ == "__main__":
    # S = "(()())(())(()(()))"
    # res = Solution().removeOuterParentheses(S)
    # print(res)

    # S = "(()())(())"
    # res = Solution().removeOuterParentheses(S)
    # print(res)

    # S = "()()"
    # res = Solution().removeOuterParentheses(S)
    # print(res)

    S = "(()())(())(()(()))"
    res = Solution().removeOuterParentheses(S)
    print(res)
