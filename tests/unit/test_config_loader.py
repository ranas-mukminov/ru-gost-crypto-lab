import pytest
import yaml
from tools.config_loader import load_config, ConfigError

def test_load_config_valid(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_data = {"key": "value", "nested": {"foo": "bar"}}
    config_file.write_text(yaml.dump(config_data))

    loaded = load_config(str(config_file))
    assert loaded == config_data

def test_load_config_missing_file():
    with pytest.raises(ConfigError):
        load_config("non_existent_file.yaml")

def test_load_config_invalid_yaml(tmp_path):
    config_file = tmp_path / "bad.yaml"
    config_file.write_text("key: value\n  indent_error: true") # Invalid YAML indentation

    with pytest.raises(ConfigError):
        load_config(str(config_file))
