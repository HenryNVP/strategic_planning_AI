"""Stub implementation for the rules engine service."""

from __future__ import annotations

import structlog

from ..models import ComplianceCheckRequest, ComplianceCheckResult

logger = structlog.get_logger(__name__)


class RulesEngineService:
    """Evaluates strategies against compliance and policy constraints."""

    def evaluate(self, payload: ComplianceCheckRequest) -> ComplianceCheckResult:
        """Run a placeholder compliance check.

        This scaffold simply echoes the request and marks the strategy as
        compliant. Replace with calls to the actual rules engine once available.
        """

        logger.info(
            "rules_engine.accepted_request",
            strategy_id=payload.strategy_id,
            constraints=len(payload.constraints),
            policies=len(payload.policies),
        )

        return ComplianceCheckResult(
            strategy_id=payload.strategy_id,
            passed=True,
            violations=[],
            details={
                "message": "Rules engine not yet implemented; returning default pass.",
                "budget_limit": payload.budget_limit,
            },
        )
