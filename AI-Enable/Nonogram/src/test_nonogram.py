"""Tests for Nonogram class functionality."""

import unittest

from nonogram import Nonogram, CellState


class NonogramTest(unittest.TestCase):

    def test_dimensions(self) -> None:
        puzzle = Nonogram(5, 5, [[1], [1], [5], [1], [1]], [[1], [1], [5], [1], [1]])
        self.assertEqual(puzzle.rows, 5)
        self.assertEqual(puzzle.cols, 5)

    def test_get_and_set_cell(self) -> None:
        puzzle = Nonogram(3, 3, [[1], [1], [1]], [[1], [1], [1]])
        self.assertEqual(puzzle.get_cell(0, 0), CellState.UNKNOWN)
        puzzle.set_cell(0, 0, CellState.FILLED)
        self.assertEqual(puzzle.get_cell(0, 0), CellState.FILLED)

    def test_extract_runs_with_trailing_empty(self) -> None:
        puzzle = Nonogram(1, 5, [[2, 1]], [[1], [1], [0], [1], [0]])
        line = [CellState.FILLED, CellState.FILLED, CellState.EMPTY, CellState.FILLED, CellState.EMPTY]
        self.assertEqual(puzzle.extract_runs(line), [2, 1])

    def test_extract_runs_empty_line(self) -> None:
        puzzle = Nonogram(1, 3, [[0]], [[0], [0], [0]])
        line = [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
        self.assertEqual(puzzle.extract_runs(line), [0])

    def test_min_line_length_single_run(self) -> None:
        puzzle = Nonogram(1, 5, [[3]], [[0], [1], [1], [1], [0]])
        self.assertEqual(puzzle.min_line_length([3]), 3)

    def test_min_line_length_empty(self) -> None:
        puzzle = Nonogram(1, 5, [[0]], [[0] for _ in range(5)])
        self.assertEqual(puzzle.min_line_length([0]), 0)

    def test_is_line_valid_complete(self) -> None:
        puzzle = Nonogram(1, 5, [[2, 1]], [[1], [1], [0], [1], [0]])
        line = [CellState.FILLED, CellState.FILLED, CellState.EMPTY, CellState.FILLED, CellState.EMPTY]
        self.assertTrue(puzzle.is_line_valid(line, [2, 1]))

    # def test_extract_runs_trailing_filled(self) -> None:
    #     puzzle = Nonogram(1, 5, [[2, 2]], [[1], [1], [0], [1], [1]])
    #     line = [CellState.FILLED, CellState.FILLED, CellState.EMPTY, CellState.FILLED, CellState.FILLED]
    #     expected = "????"
    #     self.assertEqual(puzzle.extract_runs(line), expected)

    # def test_min_line_length_multiple_runs(self) -> None:
    #     puzzle = Nonogram(1, 10, [[3, 2, 1]], [[0] for _ in range(10)])
    #     expected = "????"
    #     self.assertEqual(puzzle.min_line_length([3, 2, 1]), expected)


if __name__ == "__main__":
    unittest.main()
