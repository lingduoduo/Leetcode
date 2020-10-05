class Solution:
    def calc(self, op, left, right):
        if op == '+':
            left.update(right)
            return left
        if op == '-':
            left.subtract(right)
            return left
        ans = collections.Counter()
        for lk, lv in left.items():
            for rk, rv in right.items():
                nk = tuple(sorted(lk + rk)) if lk and rk else lk or rk
                ans[nk] += lv * rv
        return ans


    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        evaldict = {v : i for v, i, in zip(evalvars, evalints)}
        s = re.sub(r'[\d\w]+', '\g<0> ', expression)
        s = re.sub(r'\(', ' ( ', s)
        s = re.sub(r'\)', ' ) ', s)
        expression = [str(evaldict.get(t, t)) for t in s.split()]
        idx = 0
        part = collections.Counter()
        operands, operators = [part], []
        while idx < len(expression):
            e = expression[idx]
            if e == '(':
                operators.append(e)
            elif e == ')':
                while operators[-1] != '(':
                    right, left = operands.pop(), operands.pop()
                    operands.append(self.calc(operators.pop(), left, right))
                operators.pop()
            elif e in '+-':
                while operators and operators[-1] in '+-*':
                    right, left = operands.pop(), operands.pop()
                    operands.append(self.calc(operators.pop(), left, right))
                operators.append(e)
            elif e == '*':
                operators.append(e)
            else:
                part = collections.Counter()
                if e.replace('-', '').isdigit(): part[''] += int(e)
                else: part[tuple([e])] += 1
                operands.append(part)
            idx += 1
        while operators:
            right, left = operands.pop(), operands.pop()
            operands.append(self.calc(operators.pop(), left, right))
        ans = sorted(operands[-1].items(), key = lambda x: (-len(x[0]), x[0]))
        return [str(v) + (k and '*' + '*'.join(k) or '') for k, v in ans if v]
        