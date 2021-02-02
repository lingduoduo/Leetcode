class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        cnt = collections.Counter(strs)
        slist = sorted(set(strs), key=len, reverse=True)
        for i, c in enumerate(slist):
            if cnt[c] > 1: continue
            if all(self.uncommon(p, c) for p in slist[:i]):
                return len(c)
        return -1
    
    def uncommon(self, parent, child):
        lp, lc = len(parent), len(child)
        pp = pc = 0
        while pp < lp and pc < lc:
            if parent[pp] == child[pc]:
                pc += 1
            pp += 1
        return pc != lc