"""Decision hub API routes."""

from fastapi import APIRouter, Depends, status

from ...models import DecisionWorkflowRequest, DecisionWorkflowResult
from ...services import DecisionHubService, get_decision_service

router = APIRouter()


@router.post(
    "/workflows",
    response_model=DecisionWorkflowResult,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Trigger an analysis workflow",
)
def trigger_workflow(
    payload: DecisionWorkflowRequest,
    decision_service: DecisionHubService = Depends(get_decision_service),
) -> DecisionWorkflowResult:
    """Kick off a new decision workflow covering rules, scenario, and optimization stages."""

    return decision_service.run_workflow(payload)
