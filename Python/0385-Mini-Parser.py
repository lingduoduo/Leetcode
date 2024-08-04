class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        sigma, flag = None, 1
        for c in s:
            if c == "-":
                flag = -1
            elif "0" <= c <= "9":
                sigma = (sigma or 0) * 10 + int(c)
            elif c == "[":
                stack.append(NestedInteger())
            else:
                if sigma is not None:
                    stack[-1].add(NestedInteger(sigma * flag))
                    sigma, flag = None, 1
                if c == "]":
                    top = stack.pop()
                    if stack:
                        stack[-1].add(top)
                    else:
                        return top
        return NestedInteger((sigma or 0) * flag)
