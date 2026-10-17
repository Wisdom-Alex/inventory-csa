"""Reads inventory.py and prints a formatted stock report."""

from inventory import Item, inventory
from utils.helpers import (DEFAULT_LOW_STOCK_THRESHOLD, highest_stock_item,
                           low_stock_items, lowest_stock_item, total_stock_value)


def format_report(items: list[Item], threshold: int = DEFAULT_LOW_STOCK_THRESHOLD) -> str:
    """Return a table of stock lines, the total and low stock alerts."""
    lines = [f"{'Item':<12}{'Qty':>5}{'Price (NGN)':>14}{'Value (NGN)':>16}"]
    lines += [
        f"{i.item_name:<12}{i.quantity:>5}{i.price:>14,.0f}{i.value:>16,.0f}"
        for i in items
    ]
    lines += ["", f"{'Total stock value':<31}{total_stock_value(items):>16,.0f}"]
    if low := low_stock_items(items, threshold):
        names = ", ".join(i.item_name for i in low)
        lines.append(f"Low stock (<= {threshold}): {names}")
    return "\n".join(lines)


def main() -> None:
    """Print the stock report and the stock extremes."""
    print(format_report(inventory))
    print("Highest stock:", highest_stock_item(inventory).item_name)
    print("Lowest stock:", lowest_stock_item(inventory).item_name)


if __name__ == "__main__":
    main()
