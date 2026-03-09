"""Tests for Warehouse and Bin."""

import unittest

from item import Item
from warehouse import Bin, Warehouse


class WarehouseTest(unittest.TestCase):

    def test_bin_weight_check(self) -> None:
        b = Bin(0, weight_limit=10, size_limit=10)
        b.add_item(Item("A", 6, 2))
        self.assertTrue(b.can_fit(Item("B", 4, 2)))
        self.assertFalse(b.can_fit(Item("C", 5, 2)))

    def test_bin_rejects_overweight(self) -> None:
        b = Bin(0, weight_limit=5, size_limit=10)
        b.add_item(Item("A", 3, 1))
        with self.assertRaises(ValueError):
            b.add_item(Item("B", 3, 1))

    def test_warehouse_creates_bins(self) -> None:
        warehouse = Warehouse(weight_limit=10, size_limit=8)
        b1 = warehouse.create_bin()
        b2 = warehouse.create_bin()
        self.assertEqual(warehouse.total_bins(), 2)
        self.assertNotEqual(b1.bin_id, b2.bin_id)

    def test_bin_size_check(self) -> None:
        b = Bin(0, weight_limit=100, size_limit=5)
        b.add_item(Item("A", 1, 3))
        result = b.can_fit(Item("B", 1, 3))
        self.assertEqual(result, False)

    def test_remaining_size_accuracy(self) -> None:
        b = Bin(0, weight_limit=20, size_limit=10)
        b.add_item(Item("A", 8, 3))
        result = b.remaining_size()
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
