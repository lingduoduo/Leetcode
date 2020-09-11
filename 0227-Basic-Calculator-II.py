class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        curr = 0
        stack = []
        pre_op = '+'
        
        for i in range(len(s)):
            print([curr])
            print(stack)
            if s[i].isdigit():
                curr = curr * 10 + ord(s[i]) - ord('0')
            if s[i] in '+-*/' or i == len(s) - 1:
                if pre_op == '+':
                    stack.append(curr)
                elif pre_op == '-':
                    stack.append(-curr)
                elif pre_op == '*':
                    stack.append(stack.pop() * curr)
                elif pre_op == '/':
                    prev = stack.pop()
                    curr = (-1) * ((-1) * prev // curr) if prev < 0 else prev // curr
                    stack.append(curr)
                pre_op = s[i]
                curr = 0
        return sum(stack)


if __name__ == '__main__':
    ###result = Solution().calculate("3+2*2")
    ###print(result)
    ###result = Solution().calculate("3/2")
    ###print(result)
    result = Solution().calculate("14-3/2")
    print(result)
    ###result = Solution().calculate("3/2")
    ###print(result)
