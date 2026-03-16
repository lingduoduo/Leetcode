"""You'll implement this."""

from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Optional

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
        """Find all valid triples in the current grid."""
        grid = self.game.get_grid()
        positions_by_value = defaultdict(list)
        for pos, card in grid.items():
            positions_by_value[card.value].append(pos)

        valid_triples: List[List[int]] = []
        values = sorted(positions_by_value)

        for first_index, first in enumerate(values):
            for second in values[first_index:]:
                third = 15 - first - second
                if third < second or third not in positions_by_value:
                    continue

                if first == second == third:
                    for triple in combinations(positions_by_value[first], 3):
                        valid_triples.append(list(triple))
                    continue

                if first == second:
                    for same_value_pair in combinations(positions_by_value[first], 2):
                        for third_pos in positions_by_value[third]:
                            valid_triples.append([same_value_pair[0], same_value_pair[1], third_pos])
                    continue

                if second == third:
                    for first_pos in positions_by_value[first]:
                        for same_value_pair in combinations(positions_by_value[second], 2):
                            valid_triples.append([first_pos, same_value_pair[0], same_value_pair[1]])
                    continue

                for first_pos in positions_by_value[first]:
                    for second_pos in positions_by_value[second]:
                        for third_pos in positions_by_value[third]:
                            valid_triples.append([first_pos, second_pos, third_pos])
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
