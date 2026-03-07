"""Fleet definitions for Battleship."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Ship:
    name: str
    size: int


def get_test_fleet() -> List[Ship]:
    """Small fleet used by main/tests."""
    return [
        Ship("Destroyer", 2),
        Ship("Cruiser", 3),
    ]
