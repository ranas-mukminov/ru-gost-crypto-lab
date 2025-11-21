import pytest
import yaml
from tools.scenario_loader import load_scenario, ScenarioValidationError

def test_load_scenario_valid(tmp_path):
    scenario_file = tmp_path / "scenario.yaml"
    data = {
        "name": "test_scenario",
        "type": "web_tls",
        "topology": {"services": ["nginx"]},
        "test_plan": {"compatibility": True}
    }
    scenario_file.write_text(yaml.dump(data))

    scenario = load_scenario(str(scenario_file))
    assert scenario.name == "test_scenario"
    assert scenario.type == "web_tls"

def test_load_scenario_missing_required_field(tmp_path):
    scenario_file = tmp_path / "incomplete.yaml"
    data = {"name": "incomplete"} # Missing type, topology, etc.
    scenario_file.write_text(yaml.dump(data))

    with pytest.raises(ScenarioValidationError):
        load_scenario(str(scenario_file))
