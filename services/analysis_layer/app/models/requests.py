"""API request models for the analysis service."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ComplianceCheckRequest(BaseModel):
    """Request payload for the rules and compliance engine."""

    strategy_id: str = Field(..., description="Identifier for the strategy being validated.")
    constraints: list[str] = Field(default_factory=list, description="List of constraints to evaluate.")
    policies: list[str] = Field(default_factory=list, description="Policy IDs that must be satisfied.")
    budget_limit: float | None = Field(default=None, ge=0, description="Optional budget ceiling to enforce.")
    context: dict[str, Any] = Field(default_factory=dict, description="Arbitrary contextual metadata.")


class ScenarioRunRequest(BaseModel):
    """Payload describing a scenario simulation job."""

    strategy_id: str = Field(..., description="Identifier for the candidate strategy.")
    scenario_set: str = Field(..., description="Named scenario bundle to execute.")
    runs: int = Field(100, ge=1, le=10_000, description="Number of Monte Carlo runs to execute.")
    horizon_years: int = Field(5, ge=1, le=30, description="Forecast horizon for the simulation.")
    assumptions: dict[str, Any] = Field(default_factory=dict, description="Adjustable assumptions for the run.")
    parallelism: int | None = Field(
        default=None,
        ge=1,
        description="Override for default parallel run count.",
    )


class OptimizationRequest(BaseModel):
    """Input payload for optimization workloads."""

    objective: Literal["enrollment_growth", "financial_resilience", "custom"] = Field(
        "enrollment_growth",
        description="Optimization objective to maximize/minimize.",
    )
    strategy_id: str | None = Field(default=None, description="Existing strategy to refine, if any.")
    constraints: list[str] = Field(default_factory=list, description="Soft or hard constraints to honor.")
    parameters: dict[str, Any] = Field(default_factory=dict, description="Objective-specific parameters.")


class DecisionWorkflowRequest(BaseModel):
    """Orchestration payload handled by the decision hub."""

    strategy_id: str = Field(..., description="Candidate strategy identifier.")
    run_rules: bool = Field(True, description="Whether to trigger compliance validation.")
    run_scenarios: bool = Field(True, description="Whether to schedule scenario simulations.")
    run_optimization: bool = Field(False, description="Whether to run optimization loops.")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional context from upstream services.")
