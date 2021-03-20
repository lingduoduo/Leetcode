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

