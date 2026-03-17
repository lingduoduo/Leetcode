"""Tests for Solver implementation."""

import unittest
import time

from maze import Maze, Position
from mazes import (
    get_simple_maze,
    get_small_maze,
    get_medium_maze,
    get_large_maze,
    get_huge_maze,
    get_directional_maze,
    get_directional_maze_blocked,
    get_anywhere_start_end_maze,
)
from solver import Solver


class SolverTest(unittest.TestCase):

    def test_solve_simple_maze(self) -> None:
        solver = Solver(get_simple_maze())
        path = solver.solve()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], solver.maze.get_start())
        self.assertEqual(path[-1], solver.maze.get_end())

    def test_solve_medium_maze_efficiency(self) -> None:
        solver = Solver(get_medium_maze())
        t0 = time.time()
        path = solver.solve()
        elapsed = time.time() - t0
        self.assertIsNotNone(path)
        self.assertEqual(path[0], solver.maze.get_start())
        self.assertEqual(path[-1], solver.maze.get_end())
        expected_time = 10
        self.assertLess(elapsed, expected_time)

    def test_solve_large_maze_efficiency(self) -> None:
        trials = [
            (get_large_maze(20, seed=1), 1.0),
            (get_large_maze(25, seed=2), 2.0),
            (get_large_maze(30, seed=3), 3.0),
        ]
        for maze, max_time in trials:
            solver = Solver(maze)
            t0 = time.time()
            path = solver.solve()
            elapsed = time.time() - t0
            self.assertIsNotNone(path, f"No path found in {maze.rows}x{maze.cols} maze")
            self.assertLess(elapsed, max_time, f"Took {elapsed:.2f}s, expected < {max_time}s")

    def test_directional_passage_right_only(self) -> None:
        solver = Solver(get_directional_maze())
        path = solver.solve()
        self.assertIsNotNone(path)
        expected_length = 9
        self.assertEqual(len(path), expected_length)

    def test_directional_passage_blocked(self) -> None:
        solver = Solver(get_directional_maze_blocked())
        path = solver.solve()
        expected = [Position(row=1, col=1)]
        self.assertEqual(path, expected)

    def test_directional_chute_blocks_wrong_entry_side(self) -> None:
        maze = Maze(
            [
                "#######",
                "#S.#..#",
                "##>.E##",
                "#######",
            ]
        )
        solver = Solver(maze)
        path = solver.solve()
        self.assertEqual(path, [maze.get_start()])

    def test_anywhere_start_end(self) -> None:
        solver = Solver(get_anywhere_start_end_maze())
        path = solver.solve()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], solver.maze.get_start())
        self.assertEqual(path[-1], solver.maze.get_end())
        expected_length = 5
        self.assertEqual(len(path), expected_length)

    def test_key_unlocks_door_after_backtracking(self) -> None:
        maze = Maze(
            [
                "########",
                "#S.A..E#",
                "#..#.#.#",
                "#a.....#",
                "########",
            ]
        )
        solver = Solver(maze)
        path = solver.solve()
        self.assertEqual(path[0], maze.get_start())
        self.assertEqual(path[-1], maze.get_end())
        self.assertIn(Position(3, 1), path)
        self.assertIn(Position(1, 3), path)

    def test_locked_door_blocks_when_key_missing(self) -> None:
        maze = Maze(
            [
                "#####",
                "#SAE#",
                "#####",
            ]
        )
        solver = Solver(maze)
        self.assertEqual(solver.solve(), [maze.get_start()])

    def test_huge_maze_75x75(self) -> None:
        maze = get_huge_maze(75, seed=42)
        solver = Solver(maze)
        t0 = time.time()
        path = solver.solve()
        elapsed = time.time() - t0
        self.assertIsNotNone(path, "No path found in 75x75 maze")
        self.assertEqual(path[0], solver.maze.get_start())
        self.assertEqual(path[-1], solver.maze.get_end())
        expected_time = 5
        self.assertLess(elapsed, expected_time, f"75x75: {elapsed:.3f}s, need < {expected_time}s")

    def test_huge_maze_100x100(self) -> None:
        maze = get_huge_maze(100, seed=42)
        solver = Solver(maze)
        t0 = time.time()
        path = solver.solve()
        elapsed = time.time() - t0
        self.assertIsNotNone(path, "No path found in 100x100 maze")
        self.assertEqual(path[0], solver.maze.get_start())
        self.assertEqual(path[-1], solver.maze.get_end())
        expected_time = 5
        self.assertLess(elapsed, expected_time, f"100x100: {elapsed:.3f}s, need < {expected_time}s")

    def test_huge_maze_150x150(self) -> None:
        maze = get_huge_maze(150, seed=99)
        solver = Solver(maze)
        t0 = time.time()
        path = solver.solve()
        elapsed = time.time() - t0
        self.assertIsNotNone(path, "No path found in 150x150 maze")
        self.assertEqual(path[0], solver.maze.get_start())
        self.assertEqual(path[-1], solver.maze.get_end())
        expected_time = 5
        self.assertLess(elapsed, expected_time, f"150x150: {elapsed:.3f}s, need < {expected_time}s")


if __name__ == "__main__":
    unittest.main()
