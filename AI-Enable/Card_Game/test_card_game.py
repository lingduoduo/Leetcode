"""Tests for CardGame. All of this is just boilerplate to make test cases compact and understandable."""

import unittest

from card_game import CardGame
from deck import Card, Suit


class CardGameTest(unittest.TestCase):

    def test_valid_move_distinct_values(self) -> None:
        deck = [Card(9, Suit.CLUBS), Card(5, Suit.DIAMONDS), Card(1, Suit.HEARTS)]
        game = CardGame(grid_rows=1, grid_cols=3, deck=deck)
        picked = game.play_move([0, 1, 2])
        self.assertEqual(sum(c.value for c in picked), 15)

    def test_invalid_sum_rejected(self) -> None:
        deck = [Card(3, Suit.CLUBS), Card(2, Suit.DIAMONDS), Card(1, Suit.HEARTS)]
        game = CardGame(grid_rows=1, grid_cols=3, deck=deck)
        with self.assertRaises(ValueError):
            game.validate_move([0, 1, 2])

    def test_grid_refills_after_move(self) -> None:
        deck = [
            Card(7, Suit.CLUBS), Card(6, Suit.CLUBS), Card(4, Suit.CLUBS),
            Card(9, Suit.CLUBS), Card(5, Suit.DIAMONDS), Card(1, Suit.HEARTS),
        ]
        game = CardGame(grid_rows=1, grid_cols=3, deck=deck)
        game.play_move([0, 1, 2])
        self.assertEqual(len(game.get_grid()), 3)
        self.assertEqual(game.cards_remaining_in_deck(), 0)

    def test_duplicate_value_move(self) -> None:
        deck = [Card(9, Suit.DIAMONDS), Card(3, Suit.SPADES), Card(3, Suit.HEARTS)]
        game = CardGame(grid_rows=1, grid_cols=3, deck=deck)
        picked = game.play_move([0, 1, 2])
        total = sum(c.value for c in picked)
        self.assertEqual(total, 15)

    def test_triple_same_value_move(self) -> None:
        deck = [Card(5, Suit.CLUBS), Card(5, Suit.SPADES), Card(5, Suit.HEARTS)]
        game = CardGame(grid_rows=1, grid_cols=3, deck=deck)
        picked = game.play_move([0, 1, 2])
        self.assertEqual(len(picked), 3)

    def test_play_move_returns_cards_from_grid_before_refill(self) -> None:
        deck = [
            Card(7, Suit.CLUBS),
            Card(6, Suit.DIAMONDS),
            Card(2, Suit.HEARTS),
            Card(9, Suit.SPADES),
            Card(5, Suit.CLUBS),
            Card(1, Suit.DIAMONDS),
        ]
        game = CardGame(grid_rows=1, grid_cols=6, deck=deck)
        original_grid = game.get_grid()

        picked = game.play_move([3, 4, 5])

        self.assertEqual(picked, [original_grid[3], original_grid[4], original_grid[5]])
        self.assertEqual(game.history[0], [original_grid[3], original_grid[4], original_grid[5]])


if __name__ == "__main__":
    unittest.main()
