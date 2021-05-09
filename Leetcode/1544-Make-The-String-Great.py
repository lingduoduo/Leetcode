class Solution:
    def makeGood(self, s: str) -> str:
        diff = abs(ord('A') - ord('a'))
        
        stack = [s[0]]  
        for cha in s[1:]:
            if stack and abs(ord(cha) - ord(stack[-1])) == diff:
                stack.pop()
            else:
                stack.append(cha)
        return ''.join(stack)

if __name__ == '__main__':
	s = "leEeetcode"
	res = Solution().makeGood(s)
	print(res)