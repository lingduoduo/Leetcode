class Solution:
    def minSwaps(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and c == ']':
                stk.pop()
            elif c == '[':
                stk.append(c)
        return (len(stk) + 1) // 2