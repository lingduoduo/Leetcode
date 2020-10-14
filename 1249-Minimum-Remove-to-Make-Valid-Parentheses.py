class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idx = []
        stack = []

        for i in range(len(s)):
            if s[i] not in "()":
                continue
            elif s[i] == "(":
                stack.append(i)
            elif not stack:
                idx.append(i)
            else:
                stack.pop()

        res = []
        for i in range(len(s)):
            if i not in idx and i not in stack:
                res.append(s[i])
        return ''.join(res)

if __name__ == '__main__':
    s = "))(("
    results = Solution().minRemoveToMakeValid(s)
    print(results)