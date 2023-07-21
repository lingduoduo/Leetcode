class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"

        stack = []
        for n in num:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)

        for i in range(k):
            stack.pop()
        return "".join(stack).lstrip("0") or "0"


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]
        for cha in num[1:]:
            while stack and stack[-1] > cha and k >= 1:
                stack.pop()
                k -= 1
            stack.append(cha)
        res = "".join(stack[:-k] if k else stack)
        return res.lstrip("0") or "0"


if __name__ == "__main__":
    num = "1432219"
    k = 3
    res = Solution().removeKdigits(num, k)
    print(res)
