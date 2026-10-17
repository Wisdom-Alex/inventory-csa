# Inventory Tracker (Configuration Status Accounting lab)

Reads `inventory.py` and calculates the total stock value. Requires **Python 3.9 or newer** (tested on 3.9 and 3.12).

| File | Purpose |
|------|---------|
| `inventory.py` | Validated `Item` dataclass and the stock list |
| `app.py` | Formatted stock report and entry point |
| `utils/helpers.py` | Highest/lowest stock, low stock alerts, total value |
| `tests/test_inventory.py` | Unit tests (`python -m unittest -v`) |
| `changelog.txt` | Exported Git change log (commits, authors, dates) |
| `requirements.txt` | Python dependencies (standard library only) |

Run with `python app.py`.

## Commit message convention

`type(maintenance-kind): summary`, for example `fix(corrective): ...`.
This makes it possible to trace every commit to a maintenance task during
Configuration Status Accounting.
