"""Logging utilities for the analysis layer service."""

from __future__ import annotations

import logging
from typing import Any

import structlog


def configure_logging(level: int = logging.INFO) -> None:
    """Configure standard logging and structlog for the service.

    Parameters
    ----------
    level:
        Root logging level. Defaults to :data:`logging.INFO`.
    """

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.ExceptionPrettyPrinter(),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(level),
        context_class=dict[str, Any],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
