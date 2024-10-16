import yaml
from pathlib import Path

def load_config():

    project_root = Path(__file__).resolve().parent.parent 
    config_path = project_root / 'text.yaml'
    
    if not config_path.exists():
        raise FileNotFoundError(f"text.yaml не найден по пути: {config_path}")
    
    with config_path.open('r', encoding='utf-8') as file:
        return yaml.safe_load(file)

text_cfg = load_config()
