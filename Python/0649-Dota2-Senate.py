class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = collections.deque()
        qd = collections.deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                qr.append(i)
            else:
                qd.append(i)

        while qr and qd:
            r = qr.popleft()
            d = qd.popleft()
            if r < d:
                qr.append(n + r)
            else:
                qd.append(n + d)
        return "Radiant" if qr else "Dire"
