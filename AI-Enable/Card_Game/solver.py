"""You'll implement this."""

from functools import lru_cache
from itertools import combinations
from typing import Dict, List, Optional, Tuple

from card_game import CardGame


class Solver:
    """Plays the card game, maximizing the number of turns."""

    def __init__(self, game: CardGame):
        self.game = game

    def find_triple(self) -> Optional[List[int]]:
        """Find any 3 grid positions whose cards sum to 15."""
        grid = self.game.get_grid()
        positions = list(grid.keys())
        n = len(positions)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    pos1, pos2, pos3 = positions[i], positions[j], positions[k]
                    total = grid[pos1].value + grid[pos2].value + grid[pos3].value
                    if total == 15:
                        return [pos1, pos2, pos3]
        return None

    def find_all_triples(self) -> List[List[int]]:
        """Find all valid triples using only positions from the current grid."""
        grid = self.game.get_grid()
        valid_triples: List[List[int]] = []
        positions = sorted(grid)

        for triple in combinations(positions, 3):
            total = sum(grid[pos].value for pos in triple)
            if total == 15:
                valid_triples.append(list(triple))
        return valid_triples

    def play_game(self) -> int:
        """Play the game greedily until no valid moves remain."""
        turns = 0

        while self.game.has_valid_move():
            triple = self.find_triple()
            if triple is None:
                break
            self.game.play_move(triple)
            turns += 1

        return turns

    def play_game_optimized(self) -> int:
        """
        Play the game using a simple look-ahead heuristic.
        """
        return self._play_game_heuristic()

    def _play_game_heuristic(self) -> int:
        """
        Play the game using a simple look-ahead heuristic.

        For each valid move, simulate the refill and prefer the move that leaves
        the most future 3-card combinations summing to 15.
        """
        turns = 0
        grid_size = self.game.grid_rows * self.game.grid_cols

        while self.game.has_valid_move():
            valid_triples = self.find_all_triples()
            if not valid_triples:
                break

            grid = self.game.get_grid()
            best_triple: Optional[List[int]] = None
            best_score: Optional[tuple[int, int, int]] = None

            for triple in valid_triples:
                simulated_grid: Dict[int, object] = dict(grid)
                for pos in triple:
                    del simulated_grid[pos]

                simulated_deck = list(self.game._deck)
                for pos in range(grid_size):
                    if pos not in simulated_grid and simulated_deck:
                        simulated_grid[pos] = simulated_deck.pop()

                future_values = tuple(sorted(card.value for card in simulated_grid.values()))
                removed_values = sorted((grid[pos].value for pos in triple), reverse=True)
                score = (
                    self._count_combinations_with_value(15, future_values, 3),
                    sum(removed_values),
                    removed_values[0],
                )

                if best_score is None or score > best_score:
                    best_score = score
                    best_triple = triple

            if best_triple is None:
                break

            self.game.play_move(best_triple)
            turns += 1

        return turns

    def play_game_optimal(self) -> int:
        """Play the game using memoized search to maximize the turn count."""
        turns = 0

        while True:
            triple = self._find_best_triple_for_current_state()
            if triple is None:
                break
            self.game.play_move(triple)
            turns += 1

        return turns

    def _find_best_triple_for_current_state(self) -> Optional[List[int]]:
        """Choose the move that leads to the most total turns from this state."""
        grid_state = self._encode_grid_state(self.game.get_grid())
        deck_state = self._encode_deck_state()
        best_triple: Optional[List[int]] = None
        best_turns = -1

        for triple in self._get_valid_triples_from_state(grid_state):
            next_grid_state, next_deck_state = self._simulate_move(grid_state, deck_state, triple)
            total_turns = 1 + self._max_turns_from_state(next_grid_state, next_deck_state)
            if total_turns > best_turns:
                best_turns = total_turns
                best_triple = list(triple)

        return best_triple

    def _encode_grid_state(self, grid: Dict[int, object]) -> Tuple[int, ...]:
        """Encode the visible grid as card values in fixed position order."""
        return tuple(grid[pos].value if pos in grid else 0 for pos in range(self.game.grid_rows * self.game.grid_cols))

    def _encode_deck_state(self) -> Tuple[int, ...]:
        """Encode the remaining deck in pop order."""
        return tuple(card.value for card in self.game._deck)

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_valid_triples_from_state(grid_state: Tuple[int, ...]) -> Tuple[Tuple[int, int, int], ...]:
        """Enumerate all valid 3-position moves for an encoded grid."""
        positions = [pos for pos, value in enumerate(grid_state) if value != 0]
        valid_triples: List[Tuple[int, int, int]] = []

        for triple in combinations(positions, 3):
            if sum(grid_state[pos] for pos in triple) == 15:
                valid_triples.append(triple)

        return tuple(valid_triples)

    @staticmethod
    def _simulate_move(
        grid_state: Tuple[int, ...],
        deck_state: Tuple[int, ...],
        triple: Tuple[int, int, int],
    ) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        """Apply a move to an encoded state and refill from the deck."""
        next_grid = list(grid_state)
        next_deck = list(deck_state)

        for pos in triple:
            next_grid[pos] = 0

        for pos, value in enumerate(next_grid):
            if value == 0 and next_deck:
                next_grid[pos] = next_deck.pop()

        return tuple(next_grid), tuple(next_deck)

    @staticmethod
    @lru_cache(maxsize=None)
    def _max_turns_from_state(grid_state: Tuple[int, ...], deck_state: Tuple[int, ...]) -> int:
        """Return the maximum remaining turns from an encoded game state."""
        best_turns = 0

        for triple in Solver._get_valid_triples_from_state(grid_state):
            next_grid_state, next_deck_state = Solver._simulate_move(grid_state, deck_state, triple)
            best_turns = max(best_turns, 1 + Solver._max_turns_from_state(next_grid_state, next_deck_state))

        return best_turns

    def _count_combinations_with_value(self, target: int, available_values: tuple, count: int) -> int:
        """Count how many ways to make target using exactly count values."""
        if count < 0 or target < 0:
            return 0
        if count == 0:
            return 1 if target == 0 else 0

        dp = [[0] * (target + 1) for _ in range(count + 1)]
        dp[0][0] = 1

        for value in available_values:
            if value > target:
                continue
            for used in range(count - 1, -1, -1):
                for total in range(target - value, -1, -1):
                    dp[used + 1][total + value] += dp[used][total]

        return dp[count][target]

    def play_game_dp_enhanced(self) -> int:
        """Backward-compatible alias for the optimized strategy."""
        return self.play_game_optimized()

    def play_game_bitmask_dp(self) -> int:
        """Backward-compatible alias for the optimized strategy."""
        return self.play_game_optimized()

    def play_game_memoized(self) -> int:
        """Backward-compatible alias for the optimized strategy."""
        return self.play_game_optimized()
