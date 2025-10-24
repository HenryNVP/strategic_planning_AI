"""Rules engine endpoints."""

from fastapi import APIRouter, Depends, status

from ...models import ComplianceCheckRequest, ComplianceCheckResult
from ...services import RulesEngineService, get_rules_service

router = APIRouter()


@router.post(
    "/checks",
    response_model=ComplianceCheckResult,
    status_code=status.HTTP_200_OK,
    summary="Run compliance validation",
)
def run_compliance_check(
    payload: ComplianceCheckRequest,
    rules_service: RulesEngineService = Depends(get_rules_service),
) -> ComplianceCheckResult:
    """Evaluate a strategy against constraints and policies."""

    return rules_service.evaluate(payload)
