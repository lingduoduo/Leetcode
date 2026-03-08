"""Tests for Maze class functionality."""

import unittest

from maze import Maze, Position, CellType


class MazeTest(unittest.TestCase):

    def test_maze_dimensions(self) -> None:
        grid = [
            "#####",
            "#S..#",
            "#..E#",
            "#####",
        ]
        maze = Maze(grid)
        self.assertEqual(maze.rows, 4)
        self.assertEqual(maze.cols, 5)

    def test_find_start_and_end(self) -> None:
        grid = [
            "#####",
            "#S..#",
            "#..E#",
            "#####",
        ]
        maze = Maze(grid)
        self.assertEqual(maze.get_start(), Position(1, 1))
        self.assertEqual(maze.get_end(), Position(2, 3))

    def test_get_neighbors_open_space(self) -> None:
        grid = [
            "#####",
            "#S..#",
            "#...#",
            "#..E#",
            "#####",
        ]
        maze = Maze(grid)
        neighbors = maze.get_neighbors(Position(2, 2))
        positions = set(neighbors)
        self.assertIn(Position(1, 2), positions)
        self.assertIn(Position(3, 2), positions)
        self.assertIn(Position(2, 1), positions)
        self.assertIn(Position(2, 3), positions)

    def test_get_neighbors_near_wall(self) -> None:
        grid = [
            "#####",
            "#S#.#",
            "#...#",
            "#..E#",
            "#####",
        ]
        maze = Maze(grid)
        neighbors = maze.get_neighbors(Position(1, 1))
        positions = set(neighbors)
        self.assertNotIn(Position(1, 2), positions)
        self.assertIn(Position(2, 1), positions)

    def test_render_returns_original_grid(self) -> None:
        grid = [
            "#####",
            "#S..#",
            "#..E#",
            "#####",
        ]
        maze = Maze(grid)
        self.assertEqual(maze.render(), grid)

    def test_render_with_path_preserves_start_end(self) -> None:
        grid = [
            "#####",
            "#S..#",
            "#..E#",
            "#####",
        ]
        maze = Maze(grid)
        path = [Position(1, 1), Position(1, 2), Position(1, 3), Position(2, 3)]
        rendered = maze.render_with_path(path)
        expected = "*"
        self.assertEqual(rendered[1][1], expected)
        self.assertEqual(rendered[2][3], expected)

    def test_find_start_in_top_row(self) -> None:
        grid = [
            "#S..E#",
            "#....#",
            "######",
        ]
        maze = Maze(grid)
        expected =  Position(0, 1)
        self.assertEqual(maze.get_start(), expected)


if __name__ == "__main__":
    unittest.main()
