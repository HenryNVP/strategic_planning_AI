"""FastAPI entrypoint for the analysis layer service."""

from __future__ import annotations

from fastapi import FastAPI

from .api import api_router
from .core.config import settings
from .core.logging import configure_logging


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    configure_logging()
    app = FastAPI(
        title=settings.api_title,
        version=settings.api_version,
        description=settings.api_description,
    )
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
