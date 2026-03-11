"""Tests for Planner. Outlines for optional tests, maybe useful after Planner is functioning."""

import time
import unittest

from maps import get_test_map, get_standard_map, get_large_map
from planner import Planner


class PlannerTest(unittest.TestCase):

    def test_find_shortest_route(self) -> None:
        planner = Planner(get_test_map())
        route = planner.find_route("Central", "Airport")
        self.assertIsNotNone(route)
        self.assertEqual(route.stations[0], "Central")
        self.assertEqual(route.stations[-1], "Airport")
        self.assertEqual(route.total_time, 7)

    def test_transfer_limit(self) -> None:
        planner = Planner(get_standard_map())
        route = planner.find_route_with_max_transfers("Downtown", "Uptown", max_transfers=0)
        self.assertIsNotNone(route)
        self.assertEqual(route.total_time, 7)

    def test_no_route_within_transfer_limit(self) -> None:
        planner = Planner(get_standard_map())
        route = planner.find_route_with_max_transfers("Downtown", "Uptown", max_transfers=-1)
        self.assertIsNone(route)

    def test_efficiency_on_large_network(self) -> None:
        trials = [
            (get_large_map(50, 50, seed=1), "S_0_0", "S_49_49"),
            (get_large_map(60, 60, seed=2), "S_0_0", "S_59_59"),
            (get_large_map(50, 50, seed=3), "S_10_10", "S_40_40"),
        ]
        for network, start, end in trials:
            planner = Planner(network)
            t0 = time.time()
            route = planner.find_route(start, end)
            elapsed = time.time() - t0
            self.assertIsNotNone(route, f"no route from {start} to {end}")
            self.assertLess(elapsed, 2.0, f"{start}->{end} took {elapsed:.2f}s")


if __name__ == "__main__":
    unittest.main()
