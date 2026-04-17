"""Pydantic models for calculator request/response bodies."""

from pydantic import BaseModel, Field, field_validator


class SensCalculationRequest(BaseModel):
    """Defines expected input for sensitivity calculations."""

    dpi: int = Field(..., ge=100, le=20000, description="Mouse DPI value")
    sensitivity: float = Field(..., gt=0, le=10, description="In‑game sensitivity")

    @field_validator("dpi")
    @classmethod
    def validate_dpi(cls, value: int) -> int:
        """Optional additional DPI validation logic.

        This method currently returns the value unchanged but can be extended to
        enforce conventions (e.g., multiples of 50) or other domain rules.

        Args:
            value (int): Input DPI to validate.

        Returns:
            int: Sanitised DPI value.
        """
        return value


class SensCalculationResponse(BaseModel):
    """Defines the output structure for sensitivity calculations."""

    dpi: int
    sensitivity: float
    edpi: float
    cm360: float
    psa_low: float
    psa_average: float
    psa_high: float