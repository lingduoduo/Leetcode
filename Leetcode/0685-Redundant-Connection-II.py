class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def cycle(v, p):
            u = p[v]
            while u != 0:
                if u == v: return True
                u = p[u]
            return False
        
        n = len(edges)
        p = [0] * (n + 1)
        
        ans1 = []
        ans2 = []
        dup_p = False
        
        for e in edges:
            u, v = e
            if p[v] > 0:
                ans1 = [p[v], v]
                ans2 = [u, v]
                dup_p = True
                e[0] = e[1] = -1
            else:
                p[v] = u
        
        p = [0] * (n + 1)
        
        for u, v in edges:
            if u < 0: continue
            p[v] = u
            if cycle(v, p):
                return ans1 if dup_p else [u, v]
        
        return ans2
        