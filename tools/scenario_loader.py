import yaml
from pathlib import Path
from typing import List
from pydantic import BaseModel, ValidationError

class ScenarioValidationError(Exception):
    """Exception for scenario validation errors."""
    pass

class Topology(BaseModel):
    services: List[str]

class TestPlan(BaseModel):
    compatibility: bool = False
    performance: bool = False

class Scenario(BaseModel):
    name: str
    type: str
    topology: Topology
    test_plan: TestPlan

def load_scenario(path: str) -> Scenario:
    """
    Load and validate a scenario YAML file.
    
    Args:
        path: Path to the scenario YAML file.
        
    Returns:
        Validated Scenario object.
        
    Raises:
        ScenarioValidationError: If validation fails.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise ScenarioValidationError(f"Scenario file not found: {path}")
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        return Scenario(**data)
    except (yaml.YAMLError, ValidationError) as e:
        raise ScenarioValidationError(f"Invalid scenario definition in {path}: {e}")
    except Exception as e:
        raise ScenarioValidationError(f"Error reading scenario {path}: {e}")
