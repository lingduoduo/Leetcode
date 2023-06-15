class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        j = 0

        for x in pushed:
            s.append(x)
            while s and s[-1] == popped[j]:
                s.pop()
                j += 1

        return j == len(popped)
