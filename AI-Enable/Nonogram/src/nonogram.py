"""Read this first."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Sequence, Tuple


class CellState(str, Enum):
    UNKNOWN = "?"
    FILLED = "#"
    EMPTY = "."


@dataclass(slots=True)
class Nonogram:
    rows: int
    cols: int
    row_clues: Sequence[Sequence[int]]
    col_clues: Sequence[Sequence[int]]
    _grid: List[List[CellState]] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.row_clues = tuple(tuple(clue) for clue in self.row_clues)
        self.col_clues = tuple(tuple(clue) for clue in self.col_clues)
        self._grid = [
            [CellState.UNKNOWN for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def get_row_clues(self, row: int) -> List[int]:
        return list(self.row_clues[row])

    def get_col_clues(self, col: int) -> List[int]:
        return list(self.col_clues[col])

    def get_cell(self, row: int, col: int) -> CellState:
        return self._grid[row][col]

    def set_cell(self, row: int, col: int, state: CellState) -> None:
        self._grid[row][col] = state

    def get_row(self, row: int) -> List[CellState]:
        return list(self._grid[row])

    def get_col(self, col: int) -> List[CellState]:
        return [self._grid[r][col] for r in range(self.rows)]

    def is_solved(self) -> bool:
        rows_solved = all(
            self.extract_runs(self.get_row(r)) == list(self.row_clues[r])
            for r in range(self.rows)
        )
        cols_solved = all(
            self.extract_runs(self.get_col(c)) == list(self.col_clues[c])
            for c in range(self.cols)
        )
        return rows_solved and cols_solved

    def has_unknown_cells(self) -> bool:
        return any(
            cell == CellState.UNKNOWN
            for row in self._grid
            for cell in row
        )

    @staticmethod
    def extract_runs(line: Sequence[CellState]) -> List[int]:
        runs: List[int] = []
        length: int = 0
        for cell in line:
            if cell == CellState.FILLED:
                length += 1
            elif length > 0:
                runs.append(length)
                length = 0
        
        # Handle case where line ends with filled cells
        if length > 0:
            runs.append(length)
        
        return runs if runs else [0]

    @staticmethod
    def min_line_length(clues: Sequence[int]) -> int:
        if not clues or list(clues) == [0]:
            return 0
        number_of_runs = len(clues)
        return sum(clues) + (number_of_runs - 1)

    def is_line_valid(self, line: Sequence[CellState], clues: Sequence[int]) -> bool:
        if CellState.UNKNOWN in line:
            return self._is_partial_line_valid(line, clues)
        return self.extract_runs(line) == list(clues)

    def _is_partial_line_valid(self, line: Sequence[CellState], clues: Sequence[int]) -> bool:
        if self.min_line_length(clues) > len(line):
            return False

        runs: List[int] = []
        length: int = 0
        in_trailing_run: bool = False

        for cell in line:
            if cell == CellState.FILLED:
                length += 1
                in_trailing_run = True
            elif cell == CellState.EMPTY:
                if length > 0:
                    runs.append(length)
                    length = 0
                in_trailing_run = False
            else:
                break

        if in_trailing_run and length > 0:
            if len(runs) >= len(clues):
                return False
            if length > clues[len(runs)]:
                return False
        elif not in_trailing_run and length > 0:
            runs.append(length)

        for i in range(len(runs)):
            if i >= len(clues):
                return False
            if runs[i] != clues[i]:
                return False

        return True

    def clone(self) -> "Nonogram":
        new = Nonogram(self.rows, self.cols, self.row_clues, self.col_clues)
        new._grid = [row.copy() for row in self._grid]
        return new

    def render(self) -> List[str]:
        return ["".join(cell.value for cell in row) for row in self._grid]

    def render_with_clues(self) -> str:
        max_row_clue_len = max(
            len(" ".join(str(x) for x in clue)) for clue in self.row_clues
        )
        lines: List[str] = []
        for r in range(self.rows):
            clue_str = " ".join(str(x) for x in self.row_clues[r])
            padding = " " * (max_row_clue_len - len(clue_str))
            row_str = " ".join(self._grid[r][c].value for c in range(self.cols))
            lines.append(f"{padding}{clue_str} | {row_str}")

        margin = " " * (max_row_clue_len + 3)
        lines.append(margin + "-" * (self.cols * 2 - 1))

        max_depth = max(len(self.col_clues[c]) for c in range(self.cols))
        for d in range(max_depth):
            parts: List[str] = []
            for c in range(self.cols):
                clue_list = self.col_clues[c]
                offset = d - (max_depth - len(clue_list))
                if offset >= 0:
                    parts.append(str(clue_list[offset]))
                else:
                    parts.append(" ")
            lines.append(margin + " ".join(parts))

        return "\n".join(lines)
