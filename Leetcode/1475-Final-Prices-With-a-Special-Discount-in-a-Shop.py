from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        res = []
        for p in prices[::-1]:
            if p > stack[-1]:
                res.append(p - stack[-1])
                stack.append(p)
            else:
                while p < stack[-1]:
                    stack.pop()
                res.append(p - stack[-1])
                stack.append(p)
        return res[::-1]