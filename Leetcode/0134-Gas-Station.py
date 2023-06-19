from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            tank = 0
            for j in range(n):
                tank += gas[(i+j)%n] - cost[(i+j)%n]
                if tank < 0:
                    break
                if j == n - 1:
                    return i
        return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        res = 0
        for i in range(n * 2):
            tank += (gas[i % n] - cost[i % n])
            if tank >= 0:
                res += 1
            else:
                res = 0
            tank = max(0, tank)
        if res >= n:
            return 2 * n - res
        else:
            return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = remain = tot = 0
        for i in range(n):
            tot += gas[i] - cost[i]
            remain += gas[i] - cost[i]
            if remain < 0:
                remain, start = 0, i + 1
        return -1 if tot < 0 else start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = 0
        cur = 0
        res = 0

        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            cur += gas[i] - cost[i]

            if cur < 0:
                cur = 0
                res = i + 1

        return res if tot >= 0 else -1