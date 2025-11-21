import yaml
from pathlib import Path
from typing import Any, Dict

class ConfigError(Exception):
    """Base exception for configuration errors."""
    pass

def load_config(path: str) -> Dict[str, Any]:
    """
    Load a YAML configuration file.
    
    Args:
        path: Path to the YAML file.
        
    Returns:
        Dictionary containing the configuration.
        
    Raises:
        ConfigError: If the file cannot be read or contains invalid YAML.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise ConfigError(f"Configuration file not found: {path}")
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ConfigError(f"Invalid YAML in {path}: {e}")
    except Exception as e:
        raise ConfigError(f"Error reading {path}: {e}")
