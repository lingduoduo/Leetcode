from typing import List
from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        d = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            d[name][city][time] = i
            if int(amount) > 1000:
                res.add(i)
        
            for c in d[name].keys():
                if city != c:
                    for t in sorted(d[name][c].keys()):
                        if abs(int(t) - int(time)) <= 60:
                            res.add(i)
                            res.add(d[name][city][t])
        return [transactions[i] for i in list(res)]

if __name__ == '__main__':
    s = Solution()
    transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    print(s.invalidTransactions(transactions))