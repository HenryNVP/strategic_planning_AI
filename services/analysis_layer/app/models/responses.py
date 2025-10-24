"""API response models for the analysis service."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class WorkflowStatus(str, Enum):
    """Status codes for workflow execution."""

    accepted = "accepted"
    running = "running"
    completed = "completed"
    failed = "failed"


class ComplianceCheckResult(BaseModel):
    """Result payload from the rules engine."""

    strategy_id: str
    passed: bool
    violations: list[str] = Field(default_factory=list)
    details: dict[str, Any] = Field(default_factory=dict)


class ScenarioRunResult(BaseModel):
    """Result payload from scenario simulations."""

    strategy_id: str
    scenario_set: str
    metrics: dict[str, Any] = Field(default_factory=dict)
    summary: str | None = None


class OptimizationResult(BaseModel):
    """Result payload from optimization service."""

    objective: str
    recommendations: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class DecisionWorkflowResult(BaseModel):
    """Aggregate response returned by the decision hub."""

    workflow_id: str
    status: WorkflowStatus = WorkflowStatus.accepted
    strategy_id: str
    compliance: ComplianceCheckResult | None = None
    scenarios: list[ScenarioRunResult] = Field(default_factory=list)
    optimization: OptimizationResult | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
