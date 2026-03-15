"""Tests for NonogramSolver implementation."""

import time
import unittest

from puzzles import (
    get_small_puzzles,
    get_medium_puzzles,
    get_large_puzzles,
    get_huge_puzzles,
)
from solver import NonogramSolver


class SolverTest(unittest.TestCase):

    def test_solve_small_heart(self) -> None:
        puzzles = get_small_puzzles()
        solver = NonogramSolver(puzzles[0])
        result = solver.solve()
        self.assertIsNotNone(result)
        self.assertTrue(result.is_solved())

    # def test_solve_small_cross(self) -> None:
    #     puzzles = get_small_puzzles()
    #     solver = NonogramSolver(puzzles[1])
    #     result = solver.solve()
    #     self.assertIsNotNone(result)
    #     self.assertTrue(result.is_solved())

    # def test_solve_small_arrow(self) -> None:
    #     puzzles = get_small_puzzles()
    #     solver = NonogramSolver(puzzles[2])
    #     result = solver.solve()
    #     self.assertIsNotNone(result)
    #     self.assertTrue(result.is_solved())

    # def test_solve_all_small(self) -> None:
    #     for i, puzzle in enumerate(get_small_puzzles()):
    #         solver = NonogramSolver(puzzle)
    #         result = solver.solve()
    #         self.assertIsNotNone(result, f"Small puzzle {i} returned None")
    #         self.assertTrue(result.is_solved(), f"Small puzzle {i} not solved correctly")

    # def test_medium_timed(self) -> None:
    #     for i, puzzle in enumerate(get_medium_puzzles()):
    #         solver = NonogramSolver(puzzle)
    #         t0 = time.time()
    #         result = solver.solve()
    #         elapsed = time.time() - t0
    #         self.assertIsNotNone(result, f"Medium puzzle {i} returned None")
    #         self.assertTrue(result.is_solved(), f"Medium puzzle {i} not solved correctly")
    #         self.assertLess(elapsed, 5.0, f"Medium {i}: {elapsed:.2f}s, need < 5.0s")

    # def test_large_puzzle_15x15(self) -> None:
    #     puzzles = get_large_puzzles()
    #     solver = NonogramSolver(puzzles[0])
    #     t0 = time.time()
    #     result = solver.solve()
    #     elapsed = time.time() - t0
    #     self.assertIsNotNone(result, "15x15 puzzle returned None")
    #     self.assertTrue(result.is_solved(), "15x15 puzzle not solved correctly")
    #     self.assertLess(elapsed, 5.0, f"15x15: {elapsed:.2f}s, need < 5.0s")

    # def test_large_puzzle_15x15_second(self) -> None:
    #     puzzles = get_large_puzzles()
    #     solver = NonogramSolver(puzzles[1])
    #     t0 = time.time()
    #     result = solver.solve()
    #     elapsed = time.time() - t0
    #     self.assertIsNotNone(result, "15x15 puzzle 2 returned None")
    #     self.assertTrue(result.is_solved(), "15x15 puzzle 2 not solved correctly")
    #     self.assertLess(elapsed, 5.0, f"15x15: {elapsed:.2f}s, need < 5.0s")

    # def test_huge_puzzle_25x25(self) -> None:
    #     puzzles = get_huge_puzzles()
    #     solver = NonogramSolver(puzzles[0])
    #     t0 = time.time()
    #     result = solver.solve()
    #     elapsed = time.time() - t0
    #     self.assertIsNotNone(result, "25x25 puzzle returned None")
    #     self.assertTrue(result.is_solved(), "25x25 puzzle not solved correctly")
    #     self.assertLess(elapsed, 10.0, f"25x25: {elapsed:.2f}s, need < 10.0s")


if __name__ == "__main__":
    unittest.main()
