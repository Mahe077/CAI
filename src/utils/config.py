import yaml
from pathlib import Path

def load_config():
    """
    Loads the default.yaml configuration file.
    """
    config_path = Path(__file__).parent.parent.parent / "configs" / "default.yaml"
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config

if __name__ == "__main__":
    # Example of how to load the configuration
    config = load_config()
    print("Project Name:", config.get("project", {}).get("name"))
    print("Data Paths:", config.get("data"))
