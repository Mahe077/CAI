"""
Minimal config loader used by scripts/fetch_data.py and other entry points.

Provides:
- load_config(path: Optional[str]) -> dict
- get_project_root() -> pathlib.Path
"""
from pathlib import Path
from typing import Optional, Dict, Any
import json
import yaml  # type: ignore

def get_project_root() -> Path:
    # two levels up from this file -> project root
    return Path(__file__).resolve().parents[2]


def load_config(path: Optional[str] = None) -> Dict[str, Any]:
    """
    Load config from YAML or JSON. If no path given, looks for
    configs/default.yaml or configs/default.json under project root.
    Returns an empty dict if no file found.
    """
    root = get_project_root()
    if path:
        p = Path(path)
    else:
        p = root / "configs" / "default.yaml"
        if not p.exists():
            p = root / "configs" / "default.json"

    if not p.exists():
        return {}

    try:
        if p.suffix in (".yml", ".yaml"):
            return yaml.safe_load(p.read_text())
        if p.suffix == ".json":
            return json.loads(p.read_text())
    except Exception:
        return {}

    return {}
