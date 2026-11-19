"""Loading data files, with a check for missing Git LFS content."""
from pathlib import Path
import numpy as np

LFS_POINTER_PREFIX = b"version https://git-lfs"


def is_lfs_pointer(path) -> bool:
    """True if the file is a Git LFS pointer instead of the real content."""
    with open(path, "rb") as f:
        return f.read(len(LFS_POINTER_PREFIX)) == LFS_POINTER_PREFIX


def load_field(path) -> np.ndarray:
    """Load a (time, y, x) wind speed field from a .npy file."""
    path = Path(path)
    if is_lfs_pointer(path):
        raise RuntimeError(f"{path.name} is an LFS pointer, not the data. "
                           "Run `git lfs pull` in the repo.")
    return np.load(path)
