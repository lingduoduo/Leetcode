class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        while i < len(command):
            if command[i] == ")":
                if command[i - 1] == "(":
                    res.pop()
                    res.append("o")
                else:
                    res.pop()
                    res.pop()
                    res.pop()
                    res.append("a")
                    res.append("l")
            else:
                res.append(command[i])
            i += 1
        return "".join(res)
