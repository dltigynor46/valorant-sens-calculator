"""Configuration constants for the Valorant Sens Calculator.

These constants could be later extended or loaded from environment variables
if the application is expanded, but hard‑coded values work fine for the
current scope.  Separating them into a dedicated module allows for
easier maintenance and tuning.
"""

# Valorant's horizontal yaw factor (radians per unit).  This determines how
# sensitivity translates into rotational movement.  According to community
# research, a yaw of 0.07 results in consistent rotation calculations for
# 360° movements.
VALORANT_YAW: float = 0.07

# Conversion factor from inches to centimetres.
INCH_TO_CM: float = 2.54