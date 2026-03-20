"""Read this first."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple


@dataclass(frozen=True, slots=True)
class Position:
    row: int
    col: int


class CellType(str, Enum):
    WALL = "#"
    OPEN = "."
    START = "S"
    END = "E"
    PATH = "*"
    RIGHT_ONLY = ">"
    LEFT_ONLY = "<"


@dataclass
class Maze:
    grid: List[str]
    _grid: List[List[str]] = field(init=False, repr=False)
    _rows: int = field(init=False, repr=False)
    _cols: int = field(init=False, repr=False)
    _start: Position = field(init=False, repr=False)
    _end: Position = field(init=False, repr=False)

    _DIRECTIONS: Tuple[Position, ...] = (
        Position(-1, 0),
        Position(1, 0),
        Position(0, -1),
        Position(0, 1),
    )

    def __post_init__(self) -> None:
        self._grid = [list(row) for row in self.grid]
        self._rows = len(self._grid)
        self._cols = len(self._grid[0]) if self._rows > 0 else 0
        self._start = self._find_cell(CellType.START)
        self._end = self._find_cell(CellType.END)

    def _find_cell(self, cell_type: CellType) -> Position:
        for r in range(self._rows):
            for c in range(self._cols):
                if self._grid[r][c] == cell_type.value:
                    return Position(r, c)
        raise ValueError(f"No {cell_type.value} found in maze")

    def get_start(self) -> Position:
        return self._start

    def get_end(self) -> Position:
        return self._end

    def get_cell(self, pos: Position) -> str:
        return self._grid[pos.row][pos.col]

    def is_end(self, pos: Position) -> bool:
        return pos == self._end

    def _is_walkable(self, cell: str) -> bool:
        return cell in (
            CellType.OPEN.value,
            CellType.START.value,
            CellType.END.value,
            CellType.RIGHT_ONLY.value,
            CellType.LEFT_ONLY.value,
        ) or self.is_key(cell) or self.is_door(cell)

    def _can_mark_as_path(self, cell: str) -> bool:
        return cell != CellType.WALL.value

    def _render_cell(self, cell: str) -> str:
        if not cell or cell.isspace():
            return CellType.WALL.value
        return cell

    def is_key(self, cell: str) -> bool:
        return len(cell) == 1 and cell.islower()

    def is_door(self, cell: str) -> bool:
        return len(cell) == 1 and cell.isupper() and cell not in (
            CellType.START.value,
            CellType.END.value,
        )

    def is_chute(self, cell: str) -> bool:
        return cell in (CellType.RIGHT_ONLY.value, CellType.LEFT_ONLY.value)

    def is_valid_move(self, from_pos: Position, to_pos: Position) -> bool:
        if not (0 <= to_pos.row < self._rows and 0 <= to_pos.col < self._cols):
            return False

        dr = to_pos.row - from_pos.row
        dc = to_pos.col - from_pos.col
        from_cell = self.get_cell(from_pos)
        if from_cell == CellType.RIGHT_ONLY.value and (dr, dc) != (0, 1):
            return False
        if from_cell == CellType.LEFT_ONLY.value and (dr, dc) != (0, -1):
            return False

        to_cell = self.get_cell(to_pos)
        if not self._is_walkable(to_cell):
            return False

        return True

    def get_neighbors(self, pos: Position) -> List[Position]:
        neighbors: List[Position] = []

        for direction in self._DIRECTIONS:
            new_pos = Position(pos.row + direction.row, pos.col + direction.col)
            if self.is_valid_move(pos, new_pos):
                neighbors.append(new_pos)

        return neighbors

    def render(self) -> List[str]:
        return ["".join(self._render_cell(cell) for cell in row) for row in self._grid]

    def render_with_path(self, path: List[Position]) -> List[str]:
        result = [row[:] for row in self._grid]

        for pos in path:
            cell = result[pos.row][pos.col]
            if self._can_mark_as_path(cell):
                result[pos.row][pos.col] = CellType.PATH.value

        return ["".join(self._render_cell(cell) for cell in row) for row in result]

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def start(self) -> Position:
        return self._start

    @property
    def end(self) -> Position:
        return self._end
