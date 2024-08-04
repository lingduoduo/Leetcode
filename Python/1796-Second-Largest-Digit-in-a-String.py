class Solution:
    def secondHighest(self, s: str) -> int:
        firstMax = -1
        secondMax = -1
        for i in s:
            if i.isdigit():
                if secondMax < int(i) < firstMax:
                    secondMax = int(i)
                elif firstMax < int(i):
                    secondMax = firstMax
                    firstMax = int(i)

        return secondMax
