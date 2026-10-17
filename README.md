# Inventory Tracker v2.0 (re-engineered)

Modular Python package with SQLite storage, a FastAPI REST interface and Docker Compose deployment.

## Structure

| Path | Layer | Purpose |
|------|-------|---------|
| `inventory_app/models.py` | Domain | Pydantic `ItemCreate` and `Item` models |
| `inventory_app/controllers.py` | Business logic | Totals, extremes, low stock, summary |
| `inventory_app/repository.py` | Data access | All SQLite queries |
| `inventory_app/migrate.py` | Migration | JSON to SQLite (idempotent) |
| `inventory_app/api.py` | Interface | FastAPI endpoints |
| `inventory_app/cli.py` | Interface | Console report |
| `reporter/` | Second service | Calls the API and prints a report |
| `data/legacy_inventory.json` | Legacy data | Source for the migration |

## Run locally

```bash
pip install -r requirements-dev.txt
python -m inventory_app.migrate
python -m inventory_app.cli
uvicorn inventory_app.api:app --reload      # http://localhost:8000/docs
python -m unittest discover -v
```

## Run with Docker Compose

```bash
docker compose up --build
curl http://localhost:8000/summary
docker compose down
```

## Release history

| Tag | Description |
|-----|-------------|
| v0.1 | Initial baseline (seeded defects) |
| v1.0 | Corrective, adaptive, perfective, preventive maintenance |
| v2.0 | Re-engineering: modular package, SQLite, FastAPI, Docker Compose |
