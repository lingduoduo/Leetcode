class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid = set()
        
        for i, w in enumerate(s):
            if w == "(":
                stack.append(i)
            elif w == ")" and len(stack) > 0:
                valid.add(i)
                valid.add(stack[-1])
                stack.pop()
        
        res = []
        for i, w in enumerate(s):
            if w not in "()":
                res.append(w)
            elif i in valid:
                res.append(w)
        
        return "".join(res)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        res = []
        for cha in s:
            if cha == "(":
                cnt += 1
                res.append(cha)
            elif cha == ")":
                if cnt > 0:
                    cnt -= 1
                    res.append(cha)
            else:
                res.append(cha)
        
        for i in reversed(range(len(res))):
            if cnt == 0:
                break
            if res[i] == "(":
                cnt -= 1
                res[i] = ""
        return "".join(res)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        first = []
        left, right = 0, 0
        for cha in s:
            if cha not in "()":
                first.append(cha)
            elif cha == ")":
                if right > 0:
                    first.append(cha)
                    right -= 1
            else:
                first.append(cha)
                left += 1
                right += 1
        res = []
        left = left - right
        for cha in first:
            if cha == "(":
                if left > 0:
                    left -= 1
                else:
                    continue
            res.append(cha)
        return ''.join(res)


if __name__ == "__main__":
    s = "))(("
    results = Solution().minRemoveToMakeValid(s)
    print(results)
