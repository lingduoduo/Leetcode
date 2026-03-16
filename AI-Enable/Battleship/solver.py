"""You'll implement this."""

from collections import deque
from typing import Deque, List, Optional, Set, Tuple

from board import Board, ShotResult

Cell = Tuple[int, int]


class Solver:
    """Sinks all ships on a Battleship board."""

    def __init__(self, board: Board):
        self.board = board
        self.shots: List[Cell] = []
        self._tried: Set[Cell] = set()

    def _shoot(self, row: int, col: int) -> ShotResult:
        cell = (row, col)
        result = self.board.check_shot(row, col)
        self.shots.append(cell)
        self._tried.add(cell)
        return result

    def _neighbors(self, row: int, col: int) -> List[Cell]:
        candidates: List[Cell] = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.board.grid_size and 0 <= nc < self.board.grid_size:
                candidates.append((nr, nc))
        return candidates

    def _enqueue(self, targets: Deque[Cell], queued: Set[Cell], cell: Cell) -> None:
        row, col = cell
        if not (0 <= row < self.board.grid_size and 0 <= col < self.board.grid_size):
            return
        if cell in self._tried or cell in queued:
            return
        targets.append(cell)
        queued.add(cell)

    def _ship_axis(self, hits: List[Cell]) -> Optional[str]:
        if len(hits) < 2:
            return None
        if all(row == hits[0][0] for row, _ in hits):
            return "horizontal"
        if all(col == hits[0][1] for _, col in hits):
            return "vertical"
        return None

    def _extend_line_targets(
        self,
        targets: Deque[Cell],
        queued: Set[Cell],
        hits: List[Cell],
        axis: str,
    ) -> None:
        if axis == "horizontal":
            row = hits[0][0]
            cols = sorted(col for _, col in hits)
            self._enqueue(targets, queued, (row, cols[0] - 1))
            self._enqueue(targets, queued, (row, cols[-1] + 1))
            return

        col = hits[0][1]
        rows = sorted(row for row, _ in hits)
        self._enqueue(targets, queued, (rows[0] - 1, col))
        self._enqueue(targets, queued, (rows[-1] + 1, col))

    def solve(self) -> None:
        targets: Deque[Cell] = deque()
        queued: Set[Cell] = set()
        active_hits: List[Cell] = []

        # Hunt phase: probe one congruence class first so every length-3 ship
        # is guaranteed to intersect an early search cell, then fill the gaps.
        hunt_cells: List[Cell] = []
        for remainder in range(3):
            for r in range(self.board.grid_size):
                for c in range(self.board.grid_size):
                    if (r + c) % 3 == remainder:
                        hunt_cells.append((r, c))

        hunt_index = 0
        while not self.board.all_sunk():
            if targets:
                row, col = targets.popleft()
                queued.discard((row, col))
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
                queued.clear()
                active_hits.clear()
                continue

            # HIT: prioritize adjacent cells to finish this ship.
            active_hits.append((row, col))
            axis = self._ship_axis(active_hits)

            if axis is None:
                for neighbor in self._neighbors(row, col):
                    self._enqueue(targets, queued, neighbor)
                continue

            targets.clear()
            queued.clear()
            self._extend_line_targets(targets, queued, active_hits, axis)

    def get_shots(self) -> List[Tuple[int, int]]:
        return self.shots
