"""Read this first."""

from enum import Enum
from typing import List, Optional, Tuple


class CellState(str, Enum):
    UNKNOWN = "?"
    FILLED = "#"
    EMPTY = "."


class Nonogram:
    def __init__(self, rows: int, cols: int, row_clues: List[List[int]], col_clues: List[List[int]]) -> None:
        self._rows: int = rows
        self._cols: int = cols
        self._row_clues: List[List[int]] = row_clues
        self._col_clues: List[List[int]] = col_clues
        self._grid: List[List[CellState]] = [
            [CellState.UNKNOWN for _ in range(cols)] for _ in range(rows)
        ]

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def get_row_clues(self, row: int) -> List[int]:
        return self._row_clues[row]

    def get_col_clues(self, col: int) -> List[int]:
        return self._col_clues[col]

    def get_cell(self, row: int, col: int) -> CellState:
        return self._grid[row][col]

    def set_cell(self, row: int, col: int, state: CellState) -> None:
        self._grid[row][col] = state

    def get_row(self, row: int) -> List[CellState]:
        return list(self._grid[row])

    def get_col(self, col: int) -> List[CellState]:
        return [self._grid[r][col] for r in range(self._rows)]

    def is_solved(self) -> bool:
        for r in range(self._rows):
            if self.extract_runs(self.get_row(r)) != self._row_clues[r]:
                return False
        for c in range(self._cols):
            if self.extract_runs(self.get_col(c)) != self._col_clues[c]:
                return False
        return True

    def has_unknown_cells(self) -> bool:
        for r in range(self._rows):
            for c in range(self._cols):
                if self._grid[r][c] == CellState.UNKNOWN:
                    return True
        return False

    def extract_runs(self, line: List[CellState]) -> List[int]:
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

    def min_line_length(self, clues: List[int]) -> int:
        if not clues or clues == [0]:
            return 0
        number_of_runs = len(clues)
        return sum(clues) + (number_of_runs - 1)

    def is_line_valid(self, line: List[CellState], clues: List[int]) -> bool:
        if CellState.UNKNOWN in line:
            return self._is_partial_line_valid(line, clues)
        return self.extract_runs(line) == clues

    def _is_partial_line_valid(self, line: List[CellState], clues: List[int]) -> bool:
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
        new = Nonogram(self._rows, self._cols, self._row_clues, self._col_clues)
        for r in range(self._rows):
            for c in range(self._cols):
                new._grid[r][c] = self._grid[r][c]
        return new

    def render(self) -> List[str]:
        result: List[str] = []
        for r in range(self._rows):
            row_str = ""
            for c in range(self._cols):
                row_str += self._grid[r][c].value
            result.append(row_str)
        return result

    def render_with_clues(self) -> str:
        max_row_clue_len = max(
            len(" ".join(str(x) for x in clue)) for clue in self._row_clues
        )
        lines: List[str] = []
        for r in range(self._rows):
            clue_str = " ".join(str(x) for x in self._row_clues[r])
            padding = " " * (max_row_clue_len - len(clue_str))
            row_str = " ".join(self._grid[r][c].value for c in range(self._cols))
            lines.append(f"{padding}{clue_str} | {row_str}")

        margin = " " * (max_row_clue_len + 3)
        lines.append(margin + "-" * (self._cols * 2 - 1))

        max_depth = max(len(self._col_clues[c]) for c in range(self._cols))
        for d in range(max_depth):
            parts: List[str] = []
            for c in range(self._cols):
                clue_list = self._col_clues[c]
                offset = d - (max_depth - len(clue_list))
                if offset >= 0:
                    parts.append(str(clue_list[offset]))
                else:
                    parts.append(" ")
            lines.append(margin + " ".join(parts))

        return "\n".join(lines)
