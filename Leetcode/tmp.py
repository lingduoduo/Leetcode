from typing import List, Optional
import heapq

import collections


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind()
        d = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in d:
                    d[email] = i
                else:
                    dsu.union(i, d[email])

        components = {}
        for email, group in d.items():
            group_rep = dsu.find(group)
            if group_rep not in components:
                components[group_rep] = []
            components[group_rep].append(email)

        res = []
        for group, emails in components.items():
            emails.sort()
            emails = [accounts[group][0]] + emails
            res.append(emails)

        return res


class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(1001)]
        self.rank = [1] * 1001

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        else:
            if self.rank[x] >= self.rank[y]:
                self.rank[x] += self.rank[y]
                self.parent[y] = x
            else:
                self.rank[y] += self.rank[x]
                self.parent[x] = y
            return True

# Test the code        
if __name__ == '__main__':
    res = Solution().accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
    print(res)
