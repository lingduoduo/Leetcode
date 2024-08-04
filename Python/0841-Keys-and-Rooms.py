from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]

        while stack:
            idx = stack.pop(0)
            nodes = rooms[idx]
            for node in nodes:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)
        return len(visited) == len(rooms)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]

        while stack:
            key = stack.pop()
            nodes = rooms[key]
            for node in nodes:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)
        return len(visited) == len(rooms)


if __name__ == "__main__":
    res = Solution().canVisitAllRooms(rooms=[[1], [2], [3], []])
    print(res)
