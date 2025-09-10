from __future__ import annotations
from pathlib import Path
from typing import Optional

# Note: Python module names cannot contain hyphens ('-').
# We use an underscore in the module name (project_utils) instead of
# the suggested "project-utils" so it can be imported.

# Paths

def get_project_root() -> Path:
    """Return the project root (parent of src)."""
    return Path(__file__).resolve().parent.parent


def ensure_output_dir() -> Path:
    """Ensure output_qr_codes directory exists and return its Path."""
    out = get_project_root() / "output_qr_codes"
    out.mkdir(parents=True, exist_ok=True)
    return out


def resolve_input_art_path(filename: str) -> Path:
    """Return path to an asset inside images_input_art directory.
    Only the filename part is used; any provided directories are ignored.
    """
    name_only = Path(filename).name
    return get_project_root() / "images_input_art" / name_only


# Filenames

def _sanitize_stem(stem: str) -> str:
    """Make a filesystem-safe stem (no path, no extension)."""
    stem = (stem or "").strip() or "output"
    safe = "".join(c if c.isalnum() or c in "-_." else "-" for c in stem)
    # avoid empty
    return safe or "output"


def sanitize_output_filename(output_filename: Optional[str], default_stem: str) -> str:
    """Return a safe filename (no directories) guaranteed to end with .png.

    - If output_filename is provided and non-empty, its name (no directories) is used.
      If it has no extension, .png is appended.
    - Else, a default name based on default_stem (sanitized) with .png is returned.
    """
    if output_filename is not None:
        candidate = output_filename.strip()
    else:
        candidate = ""

    if candidate:
        name_only = Path(candidate).name
        if Path(name_only).suffix:
            return name_only
        return f"{name_only}.png"

    # build from default stem
    safe_stem = _sanitize_stem(default_stem)
    if not safe_stem.lower().endswith(".png"):
        return f"{safe_stem}.png"
    return safe_stem


def get_output_path(output_filename: Optional[str], default_stem: str) -> Path:
    """Return full output path under output_qr_codes for a given desired name.
    Ensures directory exists and applies sanitization rules.
    """
    out_dir = ensure_output_dir()
    name = sanitize_output_filename(output_filename, default_stem)
    return out_dir / name
