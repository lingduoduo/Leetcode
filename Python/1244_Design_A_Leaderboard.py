class Leaderboard:
    def __init__(self):
        self.d = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.d[playerId] += score    

    def top(self, K: int) -> int:
        return sum(score for _, score in self.d.most_common(K))

    def reset(self, playerId: int) -> None:
        if playerId in self.d:
            del self.d[playerId]
        