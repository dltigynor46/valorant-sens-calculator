"""Business logic for sensitivity calculations.

The CalculatorService encapsulates the core computation performed by the
application.  Separating the logic here makes it easier to test and adapt
the business rules independently of the API layer.
"""

from dataclasses import dataclass

from ..core.config import VALORANT_YAW, INCH_TO_CM


@dataclass(slots=True)
class CalculationResult:
    """Result container for sensitivity calculations.

    Stores the input DPI and sensitivity along with derived metrics.
    Using a dataclass improves readability and type hints.
    """

    dpi: int
    sensitivity: float
    edpi: float
    cm360: float
    psa_low: float
    psa_average: float
    psa_high: float


class CalculatorService:
    """Compute sensitivity metrics based on input DPI and sensitivity."""

    @staticmethod
    def calculate(dpi: int, sensitivity: float) -> CalculationResult:
        """Calculate effective DPI and related metrics.

        Args:
            dpi (int): Mouse DPI value.
            sensitivity (float): In‑game sensitivity.

        Returns:
            CalculationResult: Container with computed metrics.
        """
        # Effective DPI is simply DPI multiplied by in‑game sensitivity
        edpi = dpi * sensitivity

        # Convert to centimetres required for a 360° rotation.
        # Formula: cm/360 = (360 / (edpi * yaw)) * inches_to_cm
        cm360 = (360.0 / (edpi * VALORANT_YAW)) * INCH_TO_CM

        # PSA recommendations (80–120% of given sensitivity)
        psa_low = sensitivity * 0.8
        psa_high = sensitivity * 1.2
        psa_average = (psa_low + psa_high) / 2.0

        return CalculationResult(
            dpi=dpi,
            sensitivity=round(sensitivity, 6),
            edpi=round(edpi, 2),
            cm360=round(cm360, 2),
            psa_low=round(psa_low, 6),
            psa_average=round(psa_average, 6),
            psa_high=round(psa_high, 6),
        )