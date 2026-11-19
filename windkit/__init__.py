"""windkit: small helpers for the Colab + Git LFS demo."""
from .io import load_field, is_lfs_pointer
from .stats import summary, power_curve, capacity_factor
from .plotting import plot_mean_field, plot_timeseries

__all__ = ["load_field", "is_lfs_pointer", "summary", "power_curve",
           "capacity_factor", "plot_mean_field", "plot_timeseries"]
