class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                res.append(int(token))
            else:
                n2 = res.pop()
                n1 = res.pop()
                
            if token == '+':
                res.append(n1+n2)
            elif token == '-':
                res.append(n1-n2)
            elif token == '*':
                res.append(n1*n2)
            elif token == '/':
                res.append(int(n1/n2))

        return res[0]
