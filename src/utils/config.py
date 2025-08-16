"""
Minimal config loader used by scripts/fetch_data.py and other entry points.

Provides:
- load_config(path: Optional[str]) -> dict
- get_project_root() -> pathlib.Path
"""
from pathlib import Path
from typing import Optional, Dict, Any
import json
import os

try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # safe fallback

# optional: load .env if python-dotenv is installed
try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv(find_dotenv=True)
except Exception:
    def find_dotenv():
        return None

def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _mask(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    s = str(value)
    if len(s) <= 6:
        return "****"
    return s[:3] + "..." + s[-3:]


def load_config(path: Optional[str] = None) -> Dict[str, Any]:
    """
    Load config from YAML/JSON and merge in secrets from environment variables.
    Environment variables override file values:
      - COINGECKO_API_KEY
      - BINANCE_API_KEY
      - BINANCE_API_SECRET
    Returns config dict (secrets present in-memory), but logging helpers should mask them.
    """
    root = get_project_root()
    if path:
        p = Path(path)
    else:
        p = root / "configs" / "default.yaml"
        if not p.exists():
            p = root / "configs" / "default.json"

    cfg: Dict[str, Any] = {}
    if p.exists():
        try:
            if p.suffix in (".yml", ".yaml") and yaml is not None:
                cfg = yaml.safe_load(p.read_text()) or {}
            else:
                cfg = json.loads(p.read_text()) or {}
        except Exception:
            cfg = {}

    # Merge secrets from environment (do not persist to disk)
    data_sources = cfg.setdefault("data", {}).setdefault("data_sources", {})
    coingecko = data_sources.setdefault("coingecko", {})
    binance = data_sources.setdefault("binance", {})

    coingecko["api_key"] = os.getenv("COINGECKO_API_KEY") or coingecko.get("api_key")
    binance["api_key"] = os.getenv("BINANCE_API_KEY") or binance.get("api_key")
    binance["api_secret"] = os.getenv("BINANCE_API_SECRET") or binance.get("api_secret")

    return cfg


def get_masked_config_for_display(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Return a copy of cfg with secrets masked for safe logging."""
    out = json.loads(json.dumps(cfg))  # deep copy via serialization
    try:
        ds = out.get("data", {}).get("data_sources", {})
        if "coingecko" in ds and "api_key" in ds["coingecko"]:
            ds["coingecko"]["api_key"] = _mask(ds["coingecko"]["api_key"])
        if "binance" in ds:
            if "api_key" in ds["binance"]:
                ds["binance"]["api_key"] = _mask(ds["binance"]["api_key"])
            if "api_secret" in ds["binance"]:
                ds["binance"]["api_secret"] = _mask(ds["binance"]["api_secret"])
    except Exception:
        pass
    return out
