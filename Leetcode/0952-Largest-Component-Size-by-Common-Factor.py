class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)
            if p1 not in rank:
                rank[p1] = 0
            if p2 not in rank:
                rank[p2] = 0
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                else:
                    parent[p1] = p2
                    if rank[p1] == rank[p2]:
                        rank[p2] += 1

        def sieve(n):
            primes = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * 2, n + 1, p):
                        primes[i] = False
                p += 1
            return [element for element in range(2, n) if primes[element]]

        rank = {}
        primes = sieve(max(A) // 2 + 1)
        parent = {i: i for i in A + primes}
        for num in A:
            up = int(sqrt(num))
            t = num
            for p in primes:
                if p > up:
                    break
                if num % p == 0:
                    union(num, p)
                while t % p == 0:
                    t //= p
            if t > 1:
                union(num, t)

        return max(Counter([find(n) for n in A]).values())      
