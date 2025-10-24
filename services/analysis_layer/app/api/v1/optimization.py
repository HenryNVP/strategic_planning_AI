"""Optimization service endpoints."""

from fastapi import APIRouter, Depends, status

from ...models import OptimizationRequest, OptimizationResult
from ...services import OptimizationService, get_optimization_service

router = APIRouter()


@router.post(
    "/jobs",
    response_model=OptimizationResult,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Request an optimization run",
)
def launch_optimization(
    payload: OptimizationRequest,
    optimization_service: OptimizationService = Depends(get_optimization_service),
) -> OptimizationResult:
    """Trigger the optimization workflow for a strategy."""

    return optimization_service.optimize(payload)
