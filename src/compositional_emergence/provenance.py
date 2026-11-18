"""Inspectable provenance for source checkouts and installed distributions."""
import hashlib
import platform
from pathlib import Path
import subprocess

import numpy as np


def state_hash(state: np.ndarray) -> str:
    """SHA-256 of C-order uint8 bytes; shape is recorded separately."""
    return hashlib.sha256(np.asarray(state, dtype=np.uint8).tobytes(order="C")).hexdigest()


def source_provenance() -> dict:
    source_dir = Path(__file__).resolve().parent
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(source_dir.glob("*.py"))}
    root = source_dir.parent.parent
    git = {"revision": None, "dirty": None, "status": "not-a-source-checkout"}
    # Avoid identifying an unrelated ancestor Git repository as this package.
    if (root / "pyproject.toml").is_file() and (root / ".git").exists():
        try:
            revision = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
            status = subprocess.check_output(
                ["git", "status", "--porcelain", "--untracked-files=all"],
                cwd=root, text=True, stderr=subprocess.DEVNULL)
            git = {"revision": revision, "dirty": bool(status), "status": status.splitlines()}
        except (OSError, subprocess.CalledProcessError):
            git["status"] = "git-unavailable"
    return {"git": git, "source_sha256": hashes,
            "python": platform.python_version(), "numpy": np.__version__}
