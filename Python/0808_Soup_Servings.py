class Solution:
    def soupServings(self, N: int) -> float:
        self.d = dict()
        if N > 5000:
            return 1.0
        return self.solve(N, N)

    def solve(self, A, B):
        if (A, B) in self.d:
            return self.d[(A, B)]
        if A <= 0 and B > 0:
            return 1
        if A <= 0 and B <= 0:
            return 0.5
        if A > 0 and B <= 0:
            return 0
        prob = 0.25 * (
            self.solve(A - 100, B)
            + self.solve(A - 75, B - 25)
            + self.solve(A - 50, B - 50)
            + self.solve(A - 25, B - 75)
        )
        self.d[(A, B)] = prob
        return prob
