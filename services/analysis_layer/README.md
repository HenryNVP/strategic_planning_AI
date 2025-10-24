# Analysis Layer Service

This service coordinates strategy validation, scenario experimentation, and optimization workflows for the Strategic Planning AI stack. The current implementation is a scaffold that exposes FastAPI endpoints and stubbed service classes so the real computation backends (rules engine, EMA Workbench, optimizers) can be integrated incrementally.

## Features

- **Decision & Governance Hub** – single entrypoint that orchestrates rule checks, scenario runs, and optimization loops.
- **Rules Engine Stub** – placeholder implementation that accepts constraint payloads and issues deterministic responses.
- **Scenario Simulation Stub** – sample structure for launching EMA/Ray workloads, returning summarized metrics.
- **Optimization Stub** – demonstrates how to surface recommendations from a solver pipeline.

## Directory Layout

```
app/
  api/                 FastAPI routers (v1 endpoints)
  core/                Configuration and logging helpers
  models/              Pydantic request/response schemas
  services/            Domain service scaffolds
main.py                Uvicorn entrypoint
pyproject.toml         Service dependencies (install with `pip install -e .`)
```

## Local Development

```bash
cd services/analysis_layer
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --port 8100
```

Set environment variables with the `ANALYSIS_` prefix to customize behaviour (see `app/core/config.py`). Add actual implementations for the service methods as the rules engine, scenario runner, and optimization solver become available.
