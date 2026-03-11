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

    def test_play_game_optimized(self) -> None:
        total_turns = 0
        trials = 50
        for seed in range(trials):
            game = CardGame(grid_rows=4, grid_cols=6, seed=seed)
            solver = Solver(game)
            total_turns += solver.play_game_optimized()
        average = total_turns / trials
        self.assertGreaterEqual(average, 11.5, "optimized should average at least 11.5 turns")


if __name__ == "__main__":
    unittest.main()
