"""Command line entry point: prints the stock report from SQLite."""

from inventory_app import repository
from inventory_app.controllers import build_summary
from inventory_app.models import Item


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
    """Print the stock report from the database."""
    conn = repository.connect()
    try:
        print(format_report(repository.list_items(conn)))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
