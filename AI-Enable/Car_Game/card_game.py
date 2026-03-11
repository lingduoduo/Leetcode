"""Read this first."""

from typing import Dict, List, Optional, Set

from deck import Card, create_deck, shuffle_deck


class CardGame:
    def __init__(self, grid_rows: int = 3, grid_cols: int = 4, seed: Optional[int] = None,
                 deck: Optional[List[Card]] = None):
        self._grid_rows = grid_rows
        self._grid_cols = grid_cols
        self._grid_size = grid_rows * grid_cols
        self._grid: Dict[int, Card] = {}
        if deck is not None:
            self._deck = list(deck)
        else:
            self._deck = shuffle_deck(create_deck(), seed=seed)
        self._turns_played: int = 0
        self._history: List[List[Card]] = []
        self._fill_grid()

    @property
    def grid_rows(self) -> int:
        return self._grid_rows

    @property
    def grid_cols(self) -> int:
        return self._grid_cols

    @property
    def turns_played(self) -> int:
        return self._turns_played

    @property
    def history(self) -> List[List[Card]]:
        return list(self._history)

    def _fill_grid(self) -> None:
        for pos in range(self._grid_size):
            if pos not in self._grid and self._deck:
                self._grid[pos] = self._deck.pop()

    def get_grid(self) -> Dict[int, Card]:
        return dict(self._grid)

    def get_grid_cards(self) -> List[Card]:
        return list(self._grid.values())

    def cards_remaining_in_deck(self) -> int:
        return len(self._deck)

    def display_grid(self) -> str:
        lines: List[str] = []
        for r in range(self._grid_rows):
            row_parts: List[str] = []
            for c in range(self._grid_cols):
                pos = r * self._grid_cols + c
                if pos in self._grid:
                    row_parts.append(f"{self._grid[pos]!s:>4}")
                else:
                    row_parts.append("   .")
            lines.append(" ".join(row_parts))
        return "\n".join(lines)

    def validate_move(self, positions: List[int]) -> None:
        if len(positions) != 3:
            raise ValueError(f"Must select exactly 3 cards, got {len(positions)}")

        selected_positions: Set[int] = set()
        cards: List[Card] = []
        for pos in positions:
            if pos < 0 or pos >= self._grid_size:
                raise ValueError(f"Position {pos} is out of bounds")
            if pos not in self._grid:
                raise ValueError(f"Position {pos} is empty")
            if pos in selected_positions:
                raise ValueError(f"Duplicate position selected: {pos}")
            selected_positions.add(pos)
            cards.append(self._grid[pos])

        total = sum(card.value for card in cards)
        if total != 15:
            raise ValueError(f"Cards must sum to 15, got {total}")

    def play_move(self, positions: List[int]) -> List[Card]:
        self.validate_move(positions)
        picked: List[Card] = []
        for pos in positions:
            picked.append(self._grid.pop(pos))
        self._turns_played += 1
        self._history.append(picked)
        self._fill_grid()
        return picked

    def has_valid_move(self) -> bool:
        positions = list(self._grid.keys())
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total = (self._grid[positions[i]].value +
                             self._grid[positions[j]].value +
                             self._grid[positions[k]].value)
                    if total == 15:
                        return True
        return False
