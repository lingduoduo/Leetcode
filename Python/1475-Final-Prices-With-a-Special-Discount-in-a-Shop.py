from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
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


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        res = prices.copy()
        for i in range(1, len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prev = stack.pop()
                res[prev] = prices[prev] - prices[i]
            stack.append(i)
        return res
