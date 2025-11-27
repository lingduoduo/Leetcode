class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for cha in S:
            if not stack:
                stack.append(cha)
            elif stack[-1] != cha:
                stack.append(cha)
            else:
                stack.pop()
        return "".join(stack)


if __name__ == "__main__":
    S = "aaab"
    results = Solution().removeDuplicates(S)
    print(results)
