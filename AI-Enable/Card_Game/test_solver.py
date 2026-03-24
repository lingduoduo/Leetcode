"""Tests for Solver."""

import unittest

from card_game import CardGame
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_find_triple(self) -> None:
        game = CardGame(seed=42)
        solver = Solver(game)
        triple = solver.find_triple()
        self.assertIsNotNone(triple, "should find a triple")
        cards = [game.get_grid()[p] for p in triple]
        self.assertEqual(sum(c.value for c in cards), 15)

    def test_play_game(self) -> None:
        game = CardGame(seed=42)
        solver = Solver(game)
        turns = solver.play_game()
        self.assertGreater(turns, 0, "should play at least one turn")
        self.assertFalse(game.has_valid_move(), "game should end with no valid moves")

    def test_find_all_triples_use_only_current_grid_positions(self) -> None:
        game = CardGame(seed=42)
        solver = Solver(game)
        grid = game.get_grid()

        for triple in solver.find_all_triples():
            self.assertEqual(len(triple), 3)
            self.assertEqual(len(set(triple)), 3)
            self.assertTrue(all(pos in grid for pos in triple))
            self.assertEqual(sum(grid[pos].value for pos in triple), 15)

    def test_play_game_optimized(self) -> None:
        stats = Solver.simulate_games(
            num_games=50,
            strategy="play_game_optimized",
            grid_rows=4,
            grid_cols=6,
        )
        self.assertGreaterEqual(stats.average_turns, 11.5, "optimized should average at least 11.5 turns")

    def test_simulation_reports_full_score_count_over_100_games(self) -> None:
        stats = Solver.simulate_games(
            num_games=100,
            strategy="play_game",
            grid_rows=4,
            grid_cols=6,
        )
        self.assertEqual(stats.games_played, 100)
        self.assertEqual(stats.perfect_games, 26)
        self.assertAlmostEqual(stats.average_score, stats.average_turns * 15)

    def test_optimized_strategy_has_higher_perfect_rate(self) -> None:
        greedy_stats = Solver.simulate_games(num_games=100, strategy="play_game")
        optimized_stats = Solver.simulate_games(num_games=100, strategy="play_game_optimized")
        self.assertGreater(optimized_stats.perfect_games, greedy_stats.perfect_games)
        self.assertGreater(optimized_stats.perfect_rate, greedy_stats.perfect_rate)


if __name__ == "__main__":
    unittest.main()
