"""Root API router for the analysis service."""

from fastapi import APIRouter

from .v1 import decision, optimization, rules, scenario

api_router = APIRouter()

api_router.include_router(decision.router, prefix="/v1/decision", tags=["decision"])
api_router.include_router(rules.router, prefix="/v1/rules", tags=["rules"])
api_router.include_router(scenario.router, prefix="/v1/scenario", tags=["scenario"])
api_router.include_router(optimization.router, prefix="/v1/optimization", tags=["optimization"])
