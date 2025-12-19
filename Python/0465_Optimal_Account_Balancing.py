from typing import List, Dict, Tuple
import itertools


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = collections.defaultdict(int)
        for a, b, amount in transactions:
            balance_map[a] += amount
            balance_map[b] -= amount

        balance_list = [amount for amount in balance_map.values() if amount]
        n = len(balance_list)

        def dfs(cur):
            while cur < n and not balance_list[cur]:
                cur += 1
            if cur == n:
                return 0
            res = float('inf')
            for nxt in range(cur + 1, n):
                if balance_list[nxt] * balance_list[cur] < 0:
                    balance_list[nxt] += balance_list[cur]
                    cost = min(res, 1 + dfs(cur + 1))
                    balance_list[nxt] -= balance_list[cur]
            return res

        return dfs(0)


def tuplify(m: Dict[int, int]) -> Tuple[Tuple[int, int], ...]:
    """把 dict 变成可哈希的 tuple，便于做 memo key。"""
    # 排序保证 key 稳定（否则 dict 顺序可能导致缓存失效）
    return tuple(sorted((k, v) for k, v in m.items() if v != 0))

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        net: Dict[int, int] = {}
        for frm, to, amt in transactions:
            net[frm] = net.get(frm, 0) - amt
            net[to] = net.get(to, 0) + amt

        # 只保留非 0 的人（0 代表已经平衡，不需要参与）
        balances = {p: v for p, v in net.items() if v != 0}
        if not balances:
            return 0

        memo: Dict[Tuple[Tuple[int, int], ...], int] = {}

        def dfs(state: Tuple[Tuple[int, int], ...]) -> int:
            print(state)
            print(memo)
            """state 是 tuplify 后的 (person, balance) 列表。返回最少交易数。"""
            if not state:
                return 0
            if state in memo:
                return memo[state]

            cur = dict(state)
            people = list(cur.keys())

            # 最坏情况：n 个人需要 n-1 笔交易（链式结算）
            res = len(people) - 1

            # 2) 枚举大小为 size 的子集，如果子集净额和为 0，则该子集内部可独立结算
            for i in range(2, len(people) + 1):

                # 剪枝 A：如果当前 best 已经 <= size-1
                # 那么再找到一个 size 的零和子集，贡献至少 (size-1)，不可能让结果更小
                if res <= i - 1:
                    break

                for group in itertools.combinations(people, i):
                    if sum(cur[p] for p in group) != 0:
                        continue

                    # 把 group 拿掉，剩余部分递归求解
                    remaining = {p: bal for p, bal in cur.items() if p not in group}
                    candidate = (i - 1) + dfs(tuplify(remaining))
                    if candidate < res:
                        res = candidate

                    # 剪枝 B：如果找到 size=2 的零和对子（a+b=0）
                    # 这对人只需 1 笔交易就能完全消掉，且这是 size=2 能达到的最小贡献
                    # 在当前 size=2 的层面继续搜其他对通常收益极小，直接返回 best
                    if i == 2:
                        memo[state] = res
                        return res

            memo[state] = res
            return res

        return dfs(tuplify(balances))

if __name__ == "__main__":
    res = Solution().minTransfers(transactions = [[0,1,10],[2,0,5]])
    print(res)