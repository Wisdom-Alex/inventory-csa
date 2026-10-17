"""Second service: calls the API over HTTP and prints a stock report."""

import json
import os
import time
import urllib.request

API_URL = os.environ.get("API_URL", "http://localhost:8000")


def get(path: str):
    """GET a JSON document from the API, retrying while it starts up."""
    for attempt in range(10):
        try:
            with urllib.request.urlopen(f"{API_URL}{path}", timeout=5) as resp:
                return json.load(resp)
        except OSError:
            time.sleep(1 + attempt)
    raise SystemExit(f"API not reachable at {API_URL}")


def main() -> None:
    """Fetch items and summary, then print them."""
    items, summary = get("/items"), get("/summary")
    print(f"Reporter connected to {API_URL}")
    for i in items:
        print(f"{i['item_name']:<12}{i['quantity']:>5}{i['value']:>14,.0f}")
    print(f"Total stock value: {summary['total_stock_value']:,.0f} NGN")
    print("Low stock:", ", ".join(summary["low_stock_items"]) or "none")


if __name__ == "__main__":
    main()
