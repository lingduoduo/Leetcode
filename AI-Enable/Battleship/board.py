"""Read this first."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Set, Tuple

from fleet import Ship

Cell = Tuple[int, int]


class ShotResult(Enum):
    HIT = "HIT"
    MISS = "MISS"
    SUNK = "SUNK"


@dataclass(slots=True)
class ShipPlacement:
    ship: Ship
    cells: Tuple[Cell, ...]
    hits_remaining: int


class Board:
    def __init__(self, grid_size: int = 10):
        self._grid_size = grid_size
        self._ships: Dict[str, ShipPlacement] = {}
        self._hits: Set[Cell] = set()
        self._misses: Set[Cell] = set()
        self._ship_cells: Dict[Cell, ShipPlacement] = {}
        self._sunk: Set[str] = set()

    @property
    def grid_size(self) -> int:
        return self._grid_size

    def place_ship(self, ship: Ship, row: int, col: int, horizontal: bool) -> None:
        if ship.name in self._ships:
            raise ValueError(f"{ship.name} has already been placed")

        cells: List[Cell] = []
        for i in range(ship.size):
            if horizontal:
                r, c = row, col + i
            else:
                r, c = row + i, col
            if r < 0 or r >= self._grid_size or c < 0 or c >= self._grid_size:
                raise ValueError(f"{ship.name} out of bounds at ({r}, {c})")
            if (r, c) in self._ship_cells:
                raise ValueError(f"{ship.name} overlaps at ({r}, {c})")
            cells.append((r, c))

        placement = ShipPlacement(
            ship=ship,
            cells=tuple(cells),
            hits_remaining=ship.size,
        )
        for cell in cells:
            self._ship_cells[cell] = placement
        self._ships[ship.name] = placement

    def check_shot(self, row: int, col: int) -> ShotResult:
        cell = (row, col)
        if cell in self._hits or cell in self._misses:
            return ShotResult.MISS

        placement = self._ship_cells.get(cell)
        if placement is None:
            self._misses.add(cell)
            return ShotResult.MISS

        self._hits.add(cell)
        placement.hits_remaining -= 1
        if placement.hits_remaining == 0:
            self._sunk.add(placement.ship.name)
            return ShotResult.SUNK
        return ShotResult.HIT

    def all_sunk(self) -> bool:
        return len(self._sunk) == len(self._ships)

    def remaining_ships(self) -> int:
        return len(self._ships) - len(self._sunk)

    def total_shots(self) -> int:
        return len(self._hits) + len(self._misses)
