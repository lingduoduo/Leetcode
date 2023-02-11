from typing import List
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        self.par = [x for x in range(n)]
        nameMap = collections.defaultdict(list)

        for i, account in enumerate(accounts):
            nameMap[account[0]].append(i)

        for i in range(n):
            for j in nameMap[accounts[i][0]]:
                if (not self.same(i, j)) and (set(accounts[i][1:]) & set(accounts[j][1:])):
                    self.union(i, j)

        res = [set() for _ in range(n)]
        for i in range(n):
            self.par[i] = self.find(i)
            res[self.par[i]] |= set(accounts[i][1:])
            
        ans = []
        for i in range(n):
            if self.par[i] == i:
                person = list()
                person.append(accounts[i][0])
                person.extend(sorted(res[i]))
                ans.append(person)
        return ans
        
        
    def find(self, x):
        if x == self.par[x]:
            return self.par[x]
        parent = self.find(self.par[x])
        self.par[x] = parent
        return parent
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.par[x] = y
    
    def same(self, x, y):
        return self.find(x) == self.find(y)


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