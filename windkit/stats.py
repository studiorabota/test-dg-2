"""Simple statistics on a wind speed field."""
import numpy as np


def summary(field: np.ndarray) -> dict:
    """Basic statistics of a wind speed field in m/s."""
    return {
        "shape": field.shape,
        "mean": float(field.mean()),
        "min": float(field.min()),
        "max": float(field.max()),
        "p90": float(np.percentile(field, 90)),
    }


def power_curve(ws, cut_in=3.0, rated_ws=12.0, cut_out=25.0, rated_kw=5000.0):
    """Generic turbine power curve in kW (cubic between cut-in and rated)."""
    ws = np.asarray(ws, dtype=float)
    frac = np.clip((ws**3 - cut_in**3) / (rated_ws**3 - cut_in**3), 0, 1)
    power = frac * rated_kw
    power[(ws < cut_in) | (ws >= cut_out)] = 0.0
    return power


def capacity_factor(field: np.ndarray, rated_kw=5000.0, **curve_kwargs) -> np.ndarray:
    """Capacity factor per grid cell for a generic turbine placed there."""
    power = power_curve(field, rated_kw=rated_kw, **curve_kwargs)
    return power.mean(axis=0) / rated_kw
