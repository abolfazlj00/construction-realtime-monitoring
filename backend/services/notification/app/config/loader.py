import os
import yaml
from pathlib import Path
from pydantic import BaseModel, ValidationError

from .consumers.main import ConsumersConfig
from .providers.main import ProvidersConfig


# ============================================================
# Helper: ENV substitution
# ============================================================

def _env_interpolate(value: any) -> any:
    """
    Recursively replace ${VAR} inside strings with os.environ values.
    Supports nested lists and dicts.
    """
    if isinstance(value, str):
        if "${" in value:
            start = value.find("${")
            end = value.find("}", start)
            if end != -1:
                var_name = value[start + 2:end]
                env_value = os.getenv(var_name, "")
                return value[:start] + env_value + value[end + 1:]
        return value

    if isinstance(value, list):
        return [_env_interpolate(v) for v in value]

    if isinstance(value, dict):
        return {k: _env_interpolate(v) for k, v in value.items()}

    return value

# -----------------------------
# Root Config
# -----------------------------

class ServiceConfig(BaseModel):
    service: dict
    consumers: ConsumersConfig
    providers: ProvidersConfig
    logging: dict

    class Config:
        validate_assignment = True

# ============================================================
# Loader Function
# ============================================================
def load_service_config(path: str | Path = None) -> ServiceConfig:
    """
    Reads config.yml, performs environment variable substitution,
    and returns a typed ServiceConfig object.
    """
    if path is None:
        path = Path(__file__).resolve().parent.parent.parent / "config.yml"

    if not Path(path).exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    # Substitute environment variables like ${VAR}
    raw = _env_interpolate(raw)

    try:
        config = ServiceConfig(**raw)
    except ValidationError as e:
        raise RuntimeError(f"Invalid configuration structure:\n{e}")

    return config
