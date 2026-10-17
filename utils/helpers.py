"""Helper functions for the inventory: extremes, totals and alerts."""

from typing import Optional
from inventory import Item

DEFAULT_LOW_STOCK_THRESHOLD = 10  # units; items at or below are flagged


def highest_stock_item(items: list[Item]) -> Optional[Item]:
    """Return the item with the largest quantity, or None if empty."""
    return max(items, key=lambda i: i.quantity, default=None)


def lowest_stock_item(items: list[Item]) -> Optional[Item]:
    """Return the item with the smallest quantity, or None if empty."""
    return min(items, key=lambda i: i.quantity, default=None)


def low_stock_items(
    items: list[Item], threshold: int = DEFAULT_LOW_STOCK_THRESHOLD
) -> list[Item]:
    """Return items whose quantity is at or below ``threshold``."""
    return [i for i in items if i.quantity <= threshold]


def total_stock_value(items: list[Item]) -> float:
    """Return the sum of quantity * price for every item."""
    return sum(item.value for item in items)
