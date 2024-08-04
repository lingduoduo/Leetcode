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
        firstpass = []
        left, right = 0, 0
        for cha in s:
            if cha not in "()":
                firstpass.append(cha)
            elif cha == "(":
                left += 1
                right += 1
                firstpass.append(cha)
            else:
                if right > 0:
                    right -= 1
                    firstpass.append(cha)
        res = []
        left -= right
        for cha in firstpass:
            if cha == "(":
                if left > 0:
                    left -= 1
                else:
                    continue
            res.append(cha)
        return res


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Initialize variables
        cnt = 0
        arr = list(s)

        # First pass: mark excess closing parentheses with '*'
        for i in range(len(arr)):
            if arr[i] == '(':
                cnt += 1
            elif arr[i] == ')':
                if cnt == 0:
                    arr[i] = '*' 
                else:
                    cnt -= 1

        for i in range(len(arr) - 1, -1, -1):
            if cnt > 0 and arr[i] == '(':
                arr[i] = '*' 
                cnt -= 1
        return ''.join(c for c in arr if c != '*')
    
    
if __name__ == "__main__":
    s = "))(("
    results = Solution().minRemoveToMakeValid(s)
    print(results)
