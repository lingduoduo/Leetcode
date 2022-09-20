class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        plist = []
        while p:
            plist.append(p)
            p = p.parent
        while q:
            if q in plist:
                return q
            else:
                q = q.parent