from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return len(stack) == 0
