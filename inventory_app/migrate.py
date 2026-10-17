"""One-off migration: legacy JSON file -> SQLite database (idempotent)."""

from typing import Optional
import json
from pathlib import Path

from inventory_app import repository
from inventory_app.models import ItemCreate

LEGACY_JSON = Path(__file__).resolve().parent.parent / "data" / "legacy_inventory.json"


def migrate(json_path: Path = LEGACY_JSON, db_file: Optional[str] = None) -> int:
    """Copy JSON rows into SQLite if the table is empty; return rows inserted."""
    conn = repository.connect(db_file)
    try:
        if repository.count_items(conn) > 0:
            return 0  # already migrated, do not duplicate
        rows = json.loads(Path(json_path).read_text())
        for row in rows:
            repository.add_item(conn, ItemCreate(**row))
        return len(rows)
    finally:
        conn.close()


if __name__ == "__main__":
    inserted = migrate()
    print(f"Migration complete: {inserted} row(s) inserted into {repository.db_path()}")
