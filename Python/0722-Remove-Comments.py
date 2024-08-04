class Solution:
    """
    source = ["/*Test program */",
    "int main()",
    "{ ",
    "  // variable declaration ",
    "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ",
    "   testing */",
    "a = b + c;", "}"]
    """
from typing import List

    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        multiline = False
        line = ""
        for s in source:
            i = 0
            while i < len(s):
                if not multiline:
                    if s[i] == "/" and i < len(s) - 1 and s[i + 1] == "/":
                        break
                    elif s[i] == "/" and i < len(s) - 1 and s[i + 1] == "*":
                        multiline = True
                        i += 1
                    else:
                        line += s[i]
                else:
                    if s[i] == "*" and s[i + 1] == "/" and i < len(s) - 1:
                        multiline = False
                        i += 1
                i += 1
            if not multiline and line:
                res.append(line)
                line = ""
        return res
