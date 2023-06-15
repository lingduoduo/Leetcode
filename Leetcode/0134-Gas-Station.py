class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        remain = 0

        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]
        return start


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
