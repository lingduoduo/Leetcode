class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid = set()
        
        for i, w in enumerate(s):
            if w == "(":
                stack.append(i)
            elif w == ")" and len(stack)>0:
                valid.add(i)
                valid.add(stack[-1])
                stack.pop()
        
        res = []
        for i, w in enumerate(s):
            if w not in "()":
                res.append(w)
            elif i in valid:
                res.append(w)
        
        return ''.join(res)
    

if __name__ == '__main__':
    s = "))(("
    results = Solution().minRemoveToMakeValid(s)
    print(results)