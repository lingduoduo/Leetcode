"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from item import get_test_items
from packer import Packer
from warehouse import Warehouse


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")

    warehouse = Warehouse(weight_limit=15, size_limit=10)
    packer = Packer(warehouse)
    items = get_test_items()

    assignment = packer.pack(items)
    for name, bin_id in sorted(assignment.items(), key=lambda x: x[1]):
        print(f"  {name} -> bin {bin_id}")
    print(f"Total bins used: {warehouse.total_bins()}")
    print(f"Total items packed: {warehouse.total_items()}")

    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
