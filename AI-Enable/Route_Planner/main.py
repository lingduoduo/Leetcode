"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from maps import get_test_map
from planner import Planner


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    network = get_test_map()
    planner = Planner(network)

    route = planner.find_route("Central", "Airport")
    if route:
        print(f"Route: {' -> '.join(route.stations)}")
        print(f"Travel time: {route.total_time}")
        print(f"Transfers: {route.transfers}")
    else:
        print("No route found")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
