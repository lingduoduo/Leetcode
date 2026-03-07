"""You'll implement this."""

from collections import deque
from typing import Deque, List, Set, Tuple

from board import Board, ShotResult


class Solver:
    """Sinks all ships on a Battleship board."""

    def __init__(self, board: Board):
        self.board = board
        self.shots: List[Tuple[int, int]] = []
        self._tried: Set[Tuple[int, int]] = set()

    def _shoot(self, row: int, col: int) -> ShotResult:
        result = self.board.check_shot(row, col)
        self.shots.append((row, col))
        self._tried.add((row, col))
        return result

    def _neighbors(self, row: int, col: int) -> List[Tuple[int, int]]:
        candidates = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.board.grid_size and 0 <= nc < self.board.grid_size:
                candidates.append((nr, nc))
        return candidates

    def solve(self) -> None:
        targets: Deque[Tuple[int, int]] = deque()

        # Hunt phase: parity scan first, then the remaining cells.
        hunt_cells = [
            (r, c)
            for r in range(self.board.grid_size)
            for c in range(self.board.grid_size)
            if (r + c) % 2 == 0
        ] + [
            (r, c)
            for r in range(self.board.grid_size)
            for c in range(self.board.grid_size)
            if (r + c) % 2 == 1
        ]

        hunt_index = 0
        while not self.board.all_sunk():
            if targets:
                row, col = targets.popleft()
                if (row, col) in self._tried:
                    continue
            else:
                while hunt_index < len(hunt_cells) and hunt_cells[hunt_index] in self._tried:
                    hunt_index += 1
                if hunt_index >= len(hunt_cells):
                    break
                row, col = hunt_cells[hunt_index]
                hunt_index += 1

            result = self._shoot(row, col)
            if result == ShotResult.MISS:
                continue
            if result == ShotResult.SUNK:
                targets.clear()
                continue

            # HIT: prioritize adjacent cells to finish this ship.
            for nr, nc in self._neighbors(row, col):
                if (nr, nc) not in self._tried:
                    targets.appendleft((nr, nc))

    def get_shots(self) -> List[Tuple[int, int]]:
        return self.shots
    
