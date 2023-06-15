# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            isCelebrity = True
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    isCelebrity = False
                    break
            if isCelebrity:
                return i
        return -1
