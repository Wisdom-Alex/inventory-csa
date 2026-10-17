"""Business logic: pure functions that operate on lists of Item objects."""

from typing import Optional
from inventory_app.models import Item

DEFAULT_LOW_STOCK_THRESHOLD = 10  # units; items at or below are flagged


def total_stock_value(items: list[Item]) -> float:
    """Return the sum of quantity * price for every item."""
    return sum(i.value for i in items)


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


def build_summary(
    items: list[Item], threshold: int = DEFAULT_LOW_STOCK_THRESHOLD
) -> dict:
    """Return all headline figures in one dictionary (single source of truth)."""
    high, low = highest_stock_item(items), lowest_stock_item(items)
    return {
        "item_count": len(items),
        "total_stock_value": total_stock_value(items),
        "highest_stock": high.item_name if high else None,
        "lowest_stock": low.item_name if low else None,
        "low_stock_threshold": threshold,
        "low_stock_items": [i.item_name for i in low_stock_items(items, threshold)],
    }
