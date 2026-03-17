"""You'll implement this."""

from collections import deque
from dataclasses import dataclass
from typing import List, Optional

from maze import CellType, Maze, Position


@dataclass
class Solver:
    maze: Maze

    def _add_key(self, key_mask: int, cell: str) -> int:
        if self.maze.is_key(cell):
            return key_mask | (1 << (ord(cell) - ord("a")))
        return key_mask

    def _can_open_door(self, door: str, key_mask: int) -> bool:
        key_bit = 1 << (ord(door.lower()) - ord("a"))
        return (key_mask & key_bit) != 0

    def _is_valid_step(self, current: Position, neighbor: Position, key_mask: int) -> bool:
        if not self.maze.is_valid_move(current, neighbor):
            return False

        dr = neighbor.row - current.row
        dc = neighbor.col - current.col
        neighbor_cell = self.maze.get_cell(neighbor)

        if self.maze.is_door(neighbor_cell) and not self._can_open_door(neighbor_cell, key_mask):
            return False

        # Chutes are one-way passages: you must enter from the open side.
        if neighbor_cell == CellType.RIGHT_ONLY.value:
            return (dr, dc) == (0, 1)
        if neighbor_cell == CellType.LEFT_ONLY.value:
            return (dr, dc) == (0, -1)

        return True

    def solve(self) -> Optional[List[Position]]:
        start = self.maze.start
        end = self.maze.end
        start_keys = self._add_key(0, self.maze.get_cell(start))

        # BFS state must include carried keys because revisiting a cell
        # with more keys can unlock new branches.
        queue = deque([(start, [start], start_keys)])
        visited = {(start, start_keys)}

        while queue:
            current_pos, path, key_mask = queue.popleft()

            # Check if we reached the end
            if current_pos == end:
                return path

            for neighbor in self.maze.get_neighbors(current_pos):
                if self._is_valid_step(current_pos, neighbor, key_mask):
                    next_keys = self._add_key(key_mask, self.maze.get_cell(neighbor))
                    state = (neighbor, next_keys)
                    if state in visited:
                        continue

                    visited.add(state)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path, next_keys))

        # No path to end found - return list with just start position
        return [start]
