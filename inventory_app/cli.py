"""Command line entry point: prints the stock report."""

import json
from pathlib import Path

from inventory_app.controllers import build_summary
from inventory_app.models import Item

LEGACY_JSON = Path(__file__).resolve().parent.parent / "data" / "legacy_inventory.json"


def load_items() -> list[Item]:
    """Load items from the legacy JSON file."""
    return [Item(**row) for row in json.loads(LEGACY_JSON.read_text())]


def format_report(items: list[Item]) -> str:
    """Return a formatted table plus the summary lines."""
    s = build_summary(items)
    lines = [f"{'Item':<12}{'Qty':>5}{'Price (NGN)':>14}{'Value (NGN)':>16}"]
    lines += [
        f"{i.item_name:<12}{i.quantity:>5}{i.price:>14,.0f}{i.value:>16,.0f}"
        for i in items
    ]
    lines += ["", f"{'Total stock value':<31}{s['total_stock_value']:>16,.0f}"]
    if s["low_stock_items"]:
        lines.append(f"Low stock (<= {s['low_stock_threshold']}): "
                     + ", ".join(s["low_stock_items"]))
    return "\n".join(lines)


def main() -> None:
    """Print the stock report."""
    print(format_report(load_items()))


if __name__ == "__main__":
    main()
