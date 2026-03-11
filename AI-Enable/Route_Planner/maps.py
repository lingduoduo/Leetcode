"""
Provides sample transit maps for testing and benchmarking.
get_test_map() is useful when developing your Planner.
get_standard_map() adds one-way connections for more advanced tests.
get_large_map() generates a grid network for performance testing.
"""

from typing import List

from network import Network


def get_test_map() -> Network:
    net = Network()
    net.add_connection("Central", "Park", 4, "Green")
    net.add_connection("Park", "Airport", 6, "Green")
    net.add_connection("Central", "Mall", 2, "Blue")
    net.add_connection("Mall", "Stadium", 3, "Blue")
    net.add_connection("Stadium", "Airport", 2, "Blue")
    net.add_connection("Central", "Harbor", 5, "Red")
    net.add_connection("Harbor", "Airport", 3, "Red")
    return net


def get_standard_map() -> Network:
    net = Network()
    net.add_connection("Downtown", "Midtown", 3, "Express")
    net.add_connection("Midtown", "Uptown", 4, "Express")
    net.add_connection("Downtown", "Eastside", 2, "Crosstown")
    net.add_connection("Eastside", "Midtown", 5, "Crosstown")
    net.add_connection("Midtown", "Westside", 2, "Crosstown")
    net.add_connection("Westside", "Uptown", 3, "Crosstown")
    net.add_connection("Downtown", "Station", 1, "Shuttle")
    net.add_connection("Station", "Eastside", 1, "Shuttle")

    net.add_connection("Uptown", "Downtown", 6, "Loop", one_way=True)
    net.add_connection("Eastside", "Westside", 7, "Bypass", one_way=True)

    return net


LINES: List[str] = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]


def get_large_map(rows: int, cols: int, seed: int = 0) -> Network:
    net = Network()
    for r in range(rows):
        for c in range(cols):
            station = f"S_{r}_{c}"
            net.add_station(station)

    for r in range(rows):
        for c in range(cols):
            here = f"S_{r}_{c}"
            mix = (r * 7 + c * 13 + seed * 31) % 97

            if c + 1 < cols:
                right = f"S_{r}_{c + 1}"
                line = LINES[(r + seed) % len(LINES)]
                time = 1 + mix % 9
                net.add_connection(here, right, time, line)

            if r + 1 < rows:
                down = f"S_{r + 1}_{c}"
                line = LINES[(c + seed) % len(LINES)]
                time = 1 + (mix * 3) % 9
                net.add_connection(here, down, time, line)

    return net
