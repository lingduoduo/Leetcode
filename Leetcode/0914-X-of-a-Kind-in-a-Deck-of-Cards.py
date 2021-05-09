class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1:
            return False
        
        d = collections.Counter(deck)
        
        cnt = min(d.values())
        for i in range(2, cnt+1):
            if all(v%i==0 for v in d.values()):
                return True
        return False
        