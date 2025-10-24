"""Configuration objects for the analysis layer service."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Service-level configuration loaded from environment variables."""

    api_title: str = "Strategic Analysis API"
    api_version: str = "0.1.0"
    api_description: str = (
        "Microservice coordinating rules validation, scenario simulations, "
        "and optimization workflows for strategic planning."
    )

    # Execution knobs
    max_parallel_scenarios: int = Field(
        4,
        ge=1,
        description="Maximum number of scenario experiments to execute concurrently.",
    )
    default_timeout_seconds: int = Field(
        300,
        ge=30,
        description="Default timeout for long-running analysis tasks.",
    )
    orchestration_backend: Literal["in-memory", "celery", "ray"] = Field(
        "in-memory",
        description="Backend used to queue and orchestrate background workloads.",
    )

    # External integrations (placeholders)
    rules_engine_url: str | None = Field(default=None, description="Endpoint for a dedicated rules engine, if external.")
    scenario_runner_url: str | None = Field(
        default=None,
        description="Endpoint for external scenario simulation cluster.",
    )
    optimization_engine_url: str | None = Field(
        default=None,
        description="Endpoint for external optimization solver.",
    )

    model_config = SettingsConfigDict(env_prefix="ANALYSIS_", env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()


settings = get_settings()
