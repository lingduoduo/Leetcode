from typing import List
import collections

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        edge = defaultdict(list)
        names = {}
        for account in accounts:
            for i in range(1, len(account) - 1):
                email, nemail = account[i], account[i + 1]
                edge[email].append(nemail)
                edge[nemail].append(email)
            names[account[-1]] = account[0]

        visited = set()
        res = []
        for email, name in names.items():
            if email not in visited:
                emails = [email]
                visited.add(email)
                q = [email]
                while q:
                    e = q.pop()
                    for neighbor in edge[e]:
                        if neighbor not in visited:
                            emails.append(neighbor)
                            visited.add(neighbor)
                            q.append(neighbor)
                emails.sort()
                res.append([name] + emails)
        return res

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.par[rx] = ry
        # union by size
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.size[rx] += self.size[ry]
        
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


if __name__ == "__main__":
    res = Solution().accountsMerge(
        accounts=[
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
    # print(res)
#
# {'johnsmith@mail.com': ['john_newyork@mail.com', 'john00@mail.com'],
#  'john_newyork@mail.com': ['johnsmith@mail.com'],
#  'john00@mail.com': ['johnsmith@mail.com']}
