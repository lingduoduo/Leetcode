class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack, res = [-1], 0
        for i, e in enumerate(s):
            if e == '(':
                stack.append(i)
            elif e == ')':  # 出栈
                stack.pop()
                if not stack:  # 如果栈为空，当前 位置索引 进栈，做为一个新的子串的开始（主要用作求合法子串的长度）
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])  # 更新合法子串的长度
        return res