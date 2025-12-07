from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        d = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in d:
                    uf.union(i, d[email])
                d[email] = i

        res = defaultdict(list)
        for email, account in d.items():
            res[uf.find(account)].append(email)
        print(res)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]
        

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            return self.find(self.par[x])
    
    def union(self, x, y):
        self.par[self.find(x)] =self.find(y)


if __name__ == "__main__":
    res = Solution().accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
    print(res)