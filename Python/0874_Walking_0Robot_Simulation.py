from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 0 - N, 1 - E, 2 - S, 3 - W
        position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction]
                while command:
                    if (x + x_off, y + y_off) not in obstacles:
                        x += x_off
                        y += y_off
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        return max_distance


if __name__ == "__main__":
    commands = [4, -1, 3]
    obstacles = []
    res = Solution().robotSim(commands, obstacles)
    print(res)

    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    res = Solution().robotSim(commands, obstacles)
    print(res)
