"""Reads inventory.py and prints a formatted stock report."""

from inventory import Item, inventory
from utils.helpers import highest_stock_item, low_stock_items, lowest_stock_item


def total_stock_value(items: list[Item]) -> float:
    """Return the sum of quantity * price for every item."""
    return sum(item.value for item in items)


def format_report(items: list[Item], threshold: int = 10) -> str:
    """Return a table of stock lines, the total and low stock alerts."""
    lines = [f"{'Item':<12}{'Qty':>5}{'Price (NGN)':>14}{'Value (NGN)':>16}"]
    for i in items:
        lines.append(f"{i.item_name:<12}{i.quantity:>5}{i.price:>14,.0f}{i.value:>16,.0f}")
    lines.append("")
    lines.append(f"{'Total stock value':<31}{total_stock_value(items):>16,.0f}")
    low = low_stock_items(items, threshold)
    if low:
        lines.append("Low stock (<= %d): %s" % (threshold, ", ".join(i.item_name for i in low)))
    return "\n".join(lines)


if __name__ == "__main__":
    print(format_report(inventory))
    print("Highest stock:", highest_stock_item(inventory).item_name)
    print("Lowest stock:", lowest_stock_item(inventory).item_name)
