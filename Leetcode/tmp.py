from typing import List, Optional
import collections

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
    
if __name__ == '__main__':
    res = Solution().minRemoveToMakeValid("lee(t(c)o)de)")
    print(res)
