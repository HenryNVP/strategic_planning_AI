"""Service factory helpers for dependency injection."""

from functools import lru_cache

from .decision import DecisionHubService
from .optimization import OptimizationService
from .rules import RulesEngineService
from .scenario import ScenarioSimulationService


@lru_cache
def get_rules_service() -> RulesEngineService:
    """Return a singleton instance of :class:`RulesEngineService`."""

    return RulesEngineService()


@lru_cache
def get_scenario_service() -> ScenarioSimulationService:
    """Return a singleton instance of :class:`ScenarioSimulationService`."""

    return ScenarioSimulationService()


@lru_cache
def get_optimization_service() -> OptimizationService:
    """Return a singleton instance of :class:`OptimizationService`."""

    return OptimizationService()


@lru_cache
def get_decision_service() -> DecisionHubService:
    """Return a singleton instance of :class:`DecisionHubService`."""

    return DecisionHubService()


__all__ = [
    "DecisionHubService",
    "OptimizationService",
    "RulesEngineService",
    "ScenarioSimulationService",
    "get_decision_service",
    "get_optimization_service",
    "get_rules_service",
    "get_scenario_service",
]
