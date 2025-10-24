"""Stub implementation for the scenario simulation service."""

from __future__ import annotations

import time
import uuid

import structlog

from ..core.config import settings
from ..models import ScenarioRunRequest, ScenarioRunResult

logger = structlog.get_logger(__name__)


class ScenarioSimulationService:
    """Coordinates scenario simulations leveraging EMA workbench or similar tools."""

    def launch(self, payload: ScenarioRunRequest) -> ScenarioRunResult:
        """Launch a placeholder scenario run.

        In production this method should fan out to a worker pool or external
        simulation service. For now it returns a deterministic stub payload.
        """

        run_id = f"scenario-{uuid.uuid4()}"
        logger.info(
            "scenario.launch_stub",
            run_id=run_id,
            strategy_id=payload.strategy_id,
            scenario_set=payload.scenario_set,
            runs=payload.runs,
        )
        time.sleep(0.01)  # simulate a small amount of processing time

        metrics = {
            "expected_npv": 0.0,
            "resource_utilization": 0.0,
            "parallelism": payload.parallelism or settings.max_parallel_scenarios,
        }
        summary = (
            "Scenario simulation service scaffold. "
            "Replace with integration to EMA Workbench or preferred engine."
        )
        return ScenarioRunResult(
            strategy_id=payload.strategy_id,
            scenario_set=payload.scenario_set,
            metrics=metrics,
            summary=summary,
        )
