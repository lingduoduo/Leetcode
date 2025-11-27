class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        plist = []
        while p:
            plist.append(p)
            p = p.parent
        while q:
            if q in plist:
                return q
            else:
                q = q.parent


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1
