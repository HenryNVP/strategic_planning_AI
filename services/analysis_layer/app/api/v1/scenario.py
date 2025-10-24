"""Scenario simulation endpoints."""

from fastapi import APIRouter, Depends, status

from ...models import ScenarioRunRequest, ScenarioRunResult
from ...services import ScenarioSimulationService, get_scenario_service

router = APIRouter()


@router.post(
    "/runs",
    response_model=ScenarioRunResult,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Start a scenario simulation",
)
def launch_scenario_run(
    payload: ScenarioRunRequest,
    scenario_service: ScenarioSimulationService = Depends(get_scenario_service),
) -> ScenarioRunResult:
    """Launch a scenario simulation for the provided strategy."""

    return scenario_service.launch(payload)
