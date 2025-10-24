"""Entrypoint for running the analysis service with Uvicorn."""

from __future__ import annotations

import uvicorn

from app.main import app


def run() -> None:
    """Invoke Uvicorn using default host/port values."""

    uvicorn.run(app, host="0.0.0.0", port=8100, log_config=None)


if __name__ == "__main__":
    run()
