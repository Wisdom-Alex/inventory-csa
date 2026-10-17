"""Unit tests for the inventory modules (run: python -m unittest -v)."""

import unittest

from inventory import Item
from utils.helpers import (highest_stock_item, low_stock_items,
                           lowest_stock_item, total_stock_value)


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.items = [Item("A", 2, 100), Item("B", 10, 5), Item("C", 50, 1)]

    def test_total_uses_quantity_times_price(self):
        self.assertEqual(total_stock_value(self.items), 2 * 100 + 10 * 5 + 50 * 1)

    def test_extremes(self):
        self.assertEqual(highest_stock_item(self.items).item_name, "C")
        self.assertEqual(lowest_stock_item(self.items).item_name, "A")

    def test_empty_inventory_is_safe(self):
        self.assertEqual(total_stock_value([]), 0)
        self.assertIsNone(highest_stock_item([]))
        self.assertIsNone(lowest_stock_item([]))

    def test_low_stock_threshold(self):
        self.assertEqual([i.item_name for i in low_stock_items(self.items, 10)], ["A", "B"])

    def test_invalid_item_rejected(self):
        with self.assertRaises(ValueError):
            Item("X", -1, 10)
        with self.assertRaises(ValueError):
            Item(" ", 1, 10)


if __name__ == "__main__":
    unittest.main()
