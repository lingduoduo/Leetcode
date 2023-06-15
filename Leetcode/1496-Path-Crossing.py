class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set([(x, y)])
        for i in range(len(path)):
            if path[i] == "N":
                y += 1
            elif path[i] == "S":
                y -= 1
            elif path[i] == "E":
                x += 1
            elif path[i] == "W":
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


if __name__ == "__main__":
    path = "NES"
    results = Solution().isPathCrossing(path)
    print(results)
