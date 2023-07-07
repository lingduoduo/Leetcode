class Solution(object):
    def backspaceCompare(self, S, T):
        stack1 = []
        for s in S:
            if s == "#" and stack1:
                stack1.pop()
            elif s != "#":
                stack1.append(s)
        stack2 = []
        for s in T:
            if s == "#" and stack2:
                stack2.pop()
            elif s != "#":
                stack2.append(s)
        return stack1 == stack2


import pysnooper


@pysnooper.snoop()
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def finalstrs(strs) -> str:
            res = []
            for cha in strs:
                print(cha)
                if cha != "#":
                    res.append(cha)
                else:
                    if res:
                        res.pop()
            return "".join(res)

        fs = finalstrs(s)
        ft = finalstrs(t)
        return fs == ft


@pysnooper.snoop()
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def finalstrs(strs: str) -> str:
            skip = 0
            for x in reversed(strs):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in zip_longest(finalstrs(s), finalstrs(t)))


if __name__ == "__main__":
    # S = "ab#c"
    # T = "ad#c"
    # S = "ab##"
    # T = "c#d#"
    # S = "a##c"
    # T = "#a#c"
    # s = "a#c"
    # t = "b"
    s = "bxj##tw"
    t = "bxj###tw"
    result = Solution().backspaceCompare(s, t)
    print(result)
