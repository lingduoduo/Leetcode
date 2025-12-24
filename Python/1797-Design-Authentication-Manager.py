class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.d = defaultdict(list)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId] = [currentTime, currentTime + self.time]

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d:
            _, end = self.d[tokenId]
            if currentTime < end:
                self.d[tokenId] = [currentTime, currentTime + self.time]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for k, v in self.d.items():
            start, end = v
            if start <= currentTime < end:
                res += 1
        return res
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)